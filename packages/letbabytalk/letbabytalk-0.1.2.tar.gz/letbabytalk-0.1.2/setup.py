from setuptools import setup, find_packages
from setuptools.command.install import install
import getpass
import sys
import os

class CustomInstallCommand(install):
    def run(self):
        password = getpass.getpass('Enter the installation password: ')
        if password == 'cradleai.':
            install.run(self)
        else:
            print("Invalid password")
            sys.exit(1)

# Replace with your project name
project_name = "letbabytalk"

# Replace with your project description
project_description = "letbabytalk"

# Replace with your name
author = "Minghao Fu"

# Replace with your email
author_email = "isminghaofu@gmail.com"

# Replace with the license you're using (e.g. MIT, Apache 2.0)
license = "MIT"

# Add any requirements your project needs (e.g. ["numpy", "tensorflow"])
requirements = []

setup(
    name=project_name,
    version="0.1.2",  # Change this to your desired version
    description=project_description,
    long_description=open("README.md", "r", encoding="utf-8").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown" if os.path.exists("README.md") else None,
    author=author,
    author_email=author_email,
    license=license,
    install_requires=requirements,
    packages=find_packages(),  # Automatically finds packages in your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    # cmdclass={
    #     'install': CustomInstallCommand,
    # },
)
