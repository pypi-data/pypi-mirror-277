import os
import torch
import torch.nn as nn
import torchaudio
import re
import librosa
import pickle
import numpy as np
import random
import glob

from torch.utils.data import Dataset, DataLoader, random_split
from tqdm import tqdm

from utils import center_data, flatten_list

class SegmentedAudio(Dataset):
    def __init__(self, data):
        self.data = data
        self.len = data['audio'].shape[0]
        if len(data['audio'].shape) == 3:
            self.n_flatten_feats = data['audio'].shape[1] * data['audio'].shape[2]
        elif len(data['audio'].shape) == 2:
            self.n_flatten_feats = data['audio'].shape[-1]
        else:
            raise ValueError('Feature shape {} is not available.'.format(data['audio'].shape))
            
    def __len__(self):
        return self.len

    def __getitem__(self, idx):
        return self.data['audio'][idx], self.data['label'][idx], self.data['id'][idx], self.data['gender'][idx], self.data['age'][idx]
    
    def shape(self):
        return self.data['audio'].shape


class DonateACry:
    def __init__(self, args):
        self.data_dir = args.data_dir
        self.labels = args.labels
        self.seg_len = args.seg_len
        self.shift = args.shift
        self.n_mfcc_coeffs = args.n_mfcc_coeffs
        self.save_path = args.save_path
        self.load_path = args.load_path
        self.val_rate = args.val_rate
        self.split_type = args.split_type
        self.ages = ['04', '48', '26', '72', '22']
        self.id2audios, self.n_baby, self.baby_ids = self.get_dataset_ids()
        self.train_ids, self.val_ids = self.generate_train_val_ids(self.baby_ids, self.n_baby, self.val_rate, self.split_type, self.load_path, self.save_path)

        if self.seg_len == 1:
            train_data, val_data = self.load_one_second_audio(self.train_ids, self.val_ids, self.n_mfcc_coeffs)
        elif self.seg_len == 0:
            # 4 feature
            train_data, val_data = self.load_full_audio(self.train_ids, self.val_ids, self.n_mfcc_coeffs)
        else:
            train_data, val_data = self.load_n_seconds_audio_shift(self.seg_len, self.shift, self.train_ids, self.val_ids, self.n_mfcc_coeffs)
                
        if torch.cuda.is_available():
            for data in [train_data, val_data]:
                for k in data.keys():
                    data[k] = data[k].cuda()
        
        all_data = {'audio': [], 'label': [], 'id': []}
        all_data['audio'] = torch.cat([train_data['audio'], val_data['audio']], axis=0)
        all_data['label'] = torch.cat([train_data['label'], val_data['label']], axis=0)
        all_data['id'] = torch.cat([train_data['id'], val_data['id']], axis=0)

        self.all_data = all_data
        self.train_data = train_data
        self.val_data = val_data
        
        self.train_dataset = SegmentedAudio(train_data)
        self.val_dataset = SegmentedAudio(val_data)
        self.all_dataset = SegmentedAudio(all_data)
            
        print('Training samples: {}, validation samples: {}, total samples: {}'.format(len(self.train_dataset), \
            len(self.val_dataset), len(self.all_dataset)))
        
    def get_dataset_ids(self):
        audio_dirs = [os.path.join(self.data_dir, label) for label in self.labels]
        
        id2audios = {}
        baby_ids = []
        n_baby = 0
        for idx, dir in enumerate(audio_dirs):
            class_ids = []
            for file in os.listdir(dir):
                if file.lower().endswith(".wav"):
                    infos = file.split('-')
                    assert len(infos) == 3, "{} format is not true.".format(file)
                    id = int(infos[0])
                    if id in id2audios:
                        id2audios[id].append(file)
                    else:
                        id2audios[id] = [file]
                        class_ids.append(id)
                        n_baby += 1

            baby_ids.append(class_ids)
            
        print("--- Total baby number: {}, class distribution: {}".format(n_baby, [f"{self.labels[i]}: {len(cls)}" \
                for i, cls in enumerate(baby_ids)]))
        
        return id2audios, n_baby, baby_ids
        
    def generate_train_val_ids(self, individual_ids, n_baby, val_rate, split_type, save_path, load_path):
    
        if load_path is not None:
            with open(load_path, "rb") as file:
                data = pickle.load(file)
            train_ids = data['train']
            val_ids = data['val']
            assert len(val_ids + train_ids) == len(flatten_list(individual_ids))
            
        else:
            if split_type == 'class':
                train_ids = []
                val_ids = []
                for cls in individual_ids:
                    random.shuffle(cls)
                    n_val = int(len(cls) * val_rate)
                    val_ids.extend(cls[:n_val])
                    train_ids.extend(cls[n_val:])
                    
            elif split_type == 'baby':
                
                individual_ids = flatten_list(individual_ids)
                random.shuffle(individual_ids)
                n_val_individual = int(val_rate * n_baby)
                n_train_individuals = n_baby - n_val_individual
                train_ids = individual_ids[:n_train_individuals]
                val_ids = individual_ids[n_train_individuals:]
            
            else:
                raise ValueError('Unknow splitting type {}'.format(split_type))
            
            if save_path is not None:
                data = {'train': train_ids, 'val': val_ids}
                with open(save_path, "wb") as file:
                    pickle.dump(data, file)
        
        return train_ids, val_ids

    def load_full_audio(self, train_ids, val_ids, n_mfcc_coeffs, prefix='Full_'):
        train_data = {'audio': [], 'label': [], 'id': []}
        val_data = {'audio': [], 'label': [], 'id': []}
        full_audio_dirs = [self.data_dir + prefix + label for label in self.labels]
        print('--- Loading full audios')
        save_data=[]
        for i, dir in enumerate(full_audio_dirs):
            for file in os.listdir(dir):
                if file.lower().endswith(".wav"):
                    waveform, sample_rate = torchaudio.load(os.path.join(dir, file))
                    
                    sound_velocity = 343
                    wavelength = torch.tensor(sound_velocity / sample_rate).cuda()
                    
                    n_fft = 1024
                    win_length = None
                    hop_length = 512
                    n_mels = 256
                    n_mfcc = 256
                    spectrogram = T.Spectrogram(
                        n_fft=n_fft,
                        win_length=win_length,
                        hop_length=hop_length,
                        center=True,
                        pad_mode="reflect",
                        power=2.0,
                    )
                    spec = spectrogram(waveform)
                    
                    mfcc_transform = T.MFCC(
                        sample_rate=sample_rate,
                        n_mfcc=n_mfcc,
                        melkwargs={
                            "n_fft": n_fft,
                            "n_mels": n_mels,
                            "hop_length": hop_length,
                            "mel_scale": "htk",
                        },
                    )
                    mfcc = mfcc_transform(waveform).cuda()
                    pitch = F.detect_pitch_frequency(waveform, sample_rate).cuda()
                    
                    feature = torch.stack([mfcc.mean(), mfcc.var(), pitch.mean(), pitch.var(), wavelength], dim=0)
                    
                    id = int(re.findall(r'\d+', file)[0])
                    
                    feature_label_id = [mfcc.mean().cpu(), mfcc.var().cpu(), pitch.mean().cpu(), pitch.var().cpu(), wavelength.cpu(), i, id]
                    
                    save_data.append(feature_label_id)
                    
                    if id in train_ids:
                        train_data['audio'].append(feature)
                        train_data['label'].append(i)
                        train_data['id'].append(id)
                    elif id in val_ids:
                        val_data['audio'].append(feature)
                        val_data['label'].append(i)
                        val_data['id'].append(id)
                    else:
                        print('Data {}/{} is not included.'.format(dir, file))

            
        for data in [train_data, val_data]:
            data['audio'] =  torch.stack(data['audio'], dim=0)
            data['label'] = torch.tensor(data['label'])
            data['id'] = torch.tensor(data['id'])
            
        np.savetxt("./data.csv", np.array(save_data), delimiter=",")
        return train_data, val_data
        
    def load_one_second_audio(self, train_ids, val_ids, n_mfcc_coeffs, prefix='1s_'):
        data_idx = 0 
        train_data = {'audio': [], 'label': [], 'id': []}
        val_data = {'audio': [], 'label': [], 'id': []}
        one_second_audio_dirs = [self.data_dir + prefix + label for label in self.labels]
        print('--- Loading 1 second audios')
        for i, dir in enumerate(one_second_audio_dirs):
            for file in os.listdir(dir):
                if file.endswith(".wav"):
                    if data_idx == 1921: # dirty data
                        #print(dir + '/' + file)
                        data_idx += 1
                        continue
                    
                    y, sr = librosa.load(os.path.join(dir, file))
                    if sr != 22050:
                        print(sr, file)
                    
                    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc_coeffs).T
                    #n_frames = mfcc.shape[0]
                    pitch = np.expand_dims(librosa.yin(y, fmin=75, fmax=600), axis=1)
                    #intensity = librosa.feature.rms(y=y).flatten()
                    feature = np.concatenate((mfcc, pitch), axis=1)
                    
                    id = int(file[2:4])
                    if id in train_ids:
                        train_data['audio'].append(feature)
                        train_data['label'].append(i)
                        train_data['id'].append(id)
                    elif id in val_ids:
                        val_data['audio'].append(feature)
                        val_data['label'].append(i)
                        val_data['id'].append(id)
                    else:
                        print('Data {}/{} is not included.'.format(dir, file))
                    
                    data_idx += 1
            
        for data in [train_data, val_data]:
            data['audio'] = torch.from_numpy(center_data(np.stack(data['audio']))).float()
            data['label'] = torch.tensor(data['label'])
            data['id'] = torch.tensor(data['id'])
            
        return train_data, val_data

    def load_n_seconds_audio(self, seg_len, train_ids, val_ids, n_mfcc_coeffs):
        train_data = {'audio': [], 'label': [], 'id': []}
        val_data = {'audio': [], 'label': [], 'id': []}
        full_audio_dirs = [os.path.join(self.data_dir, label) for label in self.labels]
        print('--- Loading and segmenting {} second audios'.format(seg_len))
        for i, dir in enumerate(full_audio_dirs):
            for file in os.listdir(dir):
                if file.endswith(".wav"):
                    
                    y, sr = librosa.load(os.path.join(dir, file))
                    seg_samples = int(seg_len * sr)
                    total_segs = len(y) // seg_samples
                    id = file.split('-')[0]
                    gender = file.split('-')[1]
                    age = file.split('-')[2]
                    for seg_index in range(total_segs):
                        start = seg_index * seg_samples
                        end = (seg_index + 1) * seg_samples
                        segment = y[start:end]
                        
                        mfcc = librosa.feature.mfcc(y=segment, sr=sr, n_mfcc=n_mfcc_coeffs).T

                        #n_frames = mfcc.shape[0]
                        pitch = librosa.yin(segment, fmin=75, fmax=600)
                        #intensity = librosa.feature.rms(y=y).flatten()
                        feature = np.concatenate((mfcc, np.expand_dims(pitch, axis=1)), axis=1)
                        if id in train_ids:
                            train_data['audio'].append(feature)
                            train_data['label'].append(i)
                            train_data['id'].append(id)
                            train_data['age'].append(age)
                            train_data['gender'].append(gender)
                        elif id in val_ids:
                            val_data['audio'].append(feature)
                            val_data['label'].append(i)
                            val_data['id'].append(id)
                            val_data['age'].append(age)
                            val_data['gender'].append(gender)
                        else:
                            print('Data {}/{} is not included.'.format(dir, file))

        for data in [train_data, val_data]:
            data['audio'] = torch.from_numpy(center_data(np.stack(data['audio']))).float()
            data['label'] = torch.tensor(data['label'])
            data['id'] = torch.tensor(data['id'])
            data['age'] = torch.tensor(data['age'])
            data['gender'] = torch.tensor(data['gender'])
        
        return train_data, val_data
    
    def load_n_seconds_audio_shift(self, seg_len, shift, train_ids, val_ids, n_mfcc_coeffs, prefix='Full_'):
        train_data = {'audio': [], 'label': [], 'id': [], 'age': [], 'gender': []}
        val_data = {'audio': [], 'label': [], 'id': [], 'age': [], 'gender': []}
        full_audio_dirs = [os.path.join(self.data_dir, label) for label in self.labels]
        print('--- Loading and segmenting {} second audios with shift {} seconds'.format(seg_len, shift))
        for i, dir in enumerate(full_audio_dirs):
            for file in os.listdir(dir):
                if file.endswith(".wav"):
                    y, sr = librosa.load(os.path.join(dir, file))
                    seg_samples = int(seg_len * sr)
                    shift_samples = int(shift * sr)
                    total_segs = (len(y) - seg_samples) // shift_samples 
                    id = int(file.split('-')[0])
                    gender_idx = 0 if file.split('-')[1] == 'm' else 1
                    gender_one_hot = torch.zeros(2)
                    gender_one_hot[gender_idx] = 1
                    age_idx = self.ages.index((file.split('-')[-1]).split('.')[0])
                    age_one_hot = torch.zeros(len(self.ages))
                    age_one_hot[age_idx] = 1
                    for seg_index in range(total_segs):
                        start = seg_index * shift_samples
                        end = start + seg_samples
                        segment = y[start:end]
                        
                        mfcc = librosa.feature.mfcc(y=segment, sr=sr, n_mfcc=n_mfcc_coeffs).T

                        #n_frames = mfcc.shape[0]
                        pitch = librosa.yin(segment, fmin=75, fmax=600)
                        #intensity = librosa.feature.rms(y=y).flatten()
                        feature = np.concatenate((mfcc, np.expand_dims(pitch, axis=1)), axis=1)
                        if id in train_ids:
                            train_data['audio'].append(feature)
                            train_data['label'].append(i)
                            train_data['id'].append(id)
                            train_data['age'].append(age_one_hot)
                            train_data['gender'].append(gender_one_hot)
                        elif id in val_ids:
                            val_data['audio'].append(feature)
                            val_data['label'].append(i)
                            val_data['id'].append(id)
                            val_data['age'].append(age_one_hot)
                            val_data['gender'].append(gender_one_hot)
                        else:
                            print('Data {}/{} is not included.'.format(dir, file))

        for data in [train_data, val_data]:
            data['audio'] = torch.from_numpy(center_data(np.stack(data['audio']))).float()
            data['label'] = torch.tensor(data['label'])
            data['id'] = torch.tensor(data['id'])
            data['age'] = torch.stack(data['age'], dim=0)
            data['gender'] = torch.stack(data['gender'], dim=0)
        
        return train_data, val_data

