import os
import librosa
import numpy as np
import random
import glob
import argparse
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.models as models
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from Caulimate.Utils.Tools import seed_everything, makedir
import sys
sys.path.append('..')
from models.resnet import bin_resnet  
seed_everything(42)

DATASET_DIR = '/l/users/minghao.fu/minghao.fu/dataset'
LOG_DIR = '/l/users/minghao.fu/minghao.fu/logs'

POS_DIR_PATH = os.path.join(DATASET_DIR, 'AudioSet/unbalanced_train/Baby cry, infant cry')
NEG_DIR_PATH =  os.path.join(DATASET_DIR, 'AudioSet/balanced_train')
SAVE_DIR_PATH = os.path.join('./files/checkpoint')

N_MFCC_COEFFS = 13
WINDOW_SIZE = 100
THRESHOLD = 0.05
BATCH_SIZE = 32
LEARNING_RATE = 0.001
NUM_EPOCHS = 200

class AudioDataset(Dataset):
    def __init__(self, features, labels):
        self.features = features
        self.labels = labels
    
    def __len__(self):
        return len(self.features)
    
    def __getitem__(self, idx):
        feature = torch.tensor(self.features[idx], dtype=torch.float32)
        label = torch.tensor(self.labels[idx], dtype=torch.long)
        return feature, label

class AudioClassifier(nn.Module):
    def __init__(self, num_classes=2):
        super(AudioClassifier, self).__init__()
        self.resnet = models.resnet18(pretrained=True)
        num_ftrs = self.resnet.fc.in_features
        self.resnet.fc = nn.Linear(num_ftrs, num_classes)

    def forward(self, x):
        return self.resnet(x)
    
def get_samples(directory_path):
    samples = []
    for subdir, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.wav'):
                file_path = os.path.join(subdir, file)
                samples.append((file_path, os.path.basename(subdir)))
    return samples

def extract_features(file_path, n_mfcc_coeffs=N_MFCC_COEFFS, threshold=THRESHOLD):
    segments = []
    y, sr = librosa.load(file_path)
    # Calculate the number of frames that correspond to 2 seconds
    window_size = 2 * sr  # adjust this if you're using a different hop length
    for seg_idx, start in enumerate(range(0, len(y) - window_size + 1, window_size // 2)):
        end = start + window_size
        if end >= y.shape[0]:
            break
        seg_y = y[start:end]
        mfcc = librosa.feature.mfcc(y=seg_y, sr=sr, n_mfcc=n_mfcc_coeffs).T
        pitch = np.expand_dims(librosa.yin(seg_y, fmin=75, fmax=600), axis=1)
        feature = np.concatenate((mfcc, pitch), axis=1)
        segments.append(feature)

    return segments

def train():

    makedir(SAVE_DIR_PATH)
    negative_samples = random.sample(get_samples(NEG_DIR_PATH), 1000)
    positive_samples = random.sample(get_samples(POS_DIR_PATH), 1000)
    

    neg_features = [seg for fp, _ in tqdm(negative_samples) for seg in extract_features(fp)]

    neg_labels = [0] * len(neg_features)
   

    pos_features = [seg for fp, _ in tqdm(positive_samples) for seg in extract_features(fp)]
    pos_labels = [1] * len(pos_features)
    for each in pos_features:
        if each.shape != pos_features[0].shape:
            import pdb; pdb.set_trace()

    features = np.array(neg_features + pos_features)
    labels = np.array(neg_labels + pos_labels)

    X_train, X_val_test, y_train, y_val_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    X_test, X_val, y_test, y_val = train_test_split(X_val_test, y_val_test, test_size=0.5, random_state=42)


    train_loader = DataLoader(AudioDataset(X_train, y_train), batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(AudioDataset(X_val, y_val), batch_size=BATCH_SIZE)
    test_loader = DataLoader(AudioDataset(X_test, y_test), batch_size=BATCH_SIZE)

    model = bin_resnet()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    min_val_loss = float('inf')
    for epoch in range(NUM_EPOCHS):
        # save_epoch_path = os.path.join(SAVE_DIR_PATH, f'epoch_{epoch}') 
        # makedir(save_epoch_path)    
        model.train()
        running_loss = 0.0
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        with torch.no_grad():
            val_loss = 0.0
            for inputs, labels in val_loader:
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                val_loss += loss.item()
            if val_loss < min_val_loss:
                min_val_loss = val_loss
                print(f"{epoch} epoch, val_loss: {val_loss}, saving model to")
                torch.save(model.state_dict(), os.path.join(SAVE_DIR_PATH, f'e{epoch}_best_model.pth'))
                early_stop = 0
            else:
                early_stop += 1
            if early_stop == 10:
                break
        print(f'Epoch {epoch + 1}/{NUM_EPOCHS}, Loss: {running_loss / len(train_loader):.4f}')
        #torch.save(model.state_dict(), os.path.join(save_epoch_path, 'checkpoint.pth'))

    model.eval()
    correct = [0, 0]
    total = [0, 0]

    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            for label, prediction in zip(labels, predicted):
                total[label] += 1
                if label == prediction:
                    correct[label] += 1

    accuracy_0 = correct[0] / total[0] if total[0] > 0 else 0
    accuracy_1 = correct[1] / total[1] if total[1] > 0 else 0

    print(f'Accuracy for class 0: {accuracy_0 * 100:.2f}%')
    print(f'Accuracy for class 1: {accuracy_1 * 100:.2f}%')
    total_accuracy = sum(correct) / sum(total) if sum(total) > 0 else 0
    print(f'Total accuracy: {total_accuracy * 100:.2f}%')

def test(audio_dir='./files/audio/', ckp_path='./files/checkpoint/e17_best_model.pth'):
    audio_names = os.listdir(audio_dir)
    audio_paths = [os.path.join(audio_dir, name) for name in audio_names]
    model = bin_resnet()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    state_dict = torch.load(ckp_path, map_location=device)

    # Load the state dictionary into the model
    model.load_state_dict(state_dict)
    model.eval()
    for audio_path in audio_paths:
        seg_predicts = []
        segments = extract_features(audio_path)
        for segment in segments:
            feature_tensor = torch.from_numpy(segment).unsqueeze(0).float()
            outputs = model(feature_tensor)
            _, predicted = torch.max(outputs.data, 1)
            seg_predicts.append(predicted.item())

        vote = max(seg_predicts, key=seg_predicts.count)
        print(f'Segment predictions: {seg_predicts}, vote result: {vote}')

def main():
    parser = argparse.ArgumentParser(description='Train or test the model')
    parser.add_argument('--mode', type=str, choices=['train', 'test'], default='train',
                        help='Mode to run: "train" or "test"')

    args = parser.parse_args()

    if args.mode == 'train':
        train()
    elif args.mode == 'test':
        test()  # Assume you have a function called test

if __name__ == '__main__':
    main()
