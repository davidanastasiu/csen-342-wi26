# Utility functions for tutorials
import os
import torchvision
from torchvision.datasets import FashionMNIST

def download_fashion_mnist(data_root='../data'):
    # Check if FashionMNIST is already downloaded
    dataset_path = os.path.join(data_root, 'FashionMNIST')
    if os.path.exists(dataset_path):
        return
    
    # Define where torchvision expects the files (It creates a subfolder matching the class name)
    fmnist_dir = os.path.join(data_root, 'FashionMNIST', 'raw')

    # Ensure directory exists
    os.makedirs(fmnist_dir, exist_ok=True)

    # List of files required by FashionMNIST
    base_url = "http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/"
    files = [
        "train-images-idx3-ubyte.gz",
        "train-labels-idx1-ubyte.gz",
        "t10k-images-idx3-ubyte.gz",
        "t10k-labels-idx1-ubyte.gz"
    ]

    # Download manually if missing
    for filename in files:
        filepath = os.path.join(fmnist_dir, filename)
        if not os.path.exists(filepath):
            print(f"Downloading {filename}...")
            url = base_url + filename
            # Use !wget if in Jupyter, or os.system for pure python
            os.system(f"wget -q -O {filepath} {url}")


def download_cifar10(data_root='../data'):
    """
    Downloads CIFAR-10 dataset manually via wget to bypass 
    compute node firewall restrictions.
    """
    # Create directory if it doesn't exist
    os.makedirs(data_root, exist_ok=True)
    
    # Check for the specific file torchvision looks for
    # torchvision extracts to 'cifar-10-batches-py'
    tar_path = os.path.join(data_root, 'cifar-10-python.tar.gz')
    extract_path = os.path.join(data_root, 'cifar-10-batches-py')
    
    if not os.path.exists(extract_path) and not os.path.exists(tar_path):
        url = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
        # -nc: no clobber (don't download if exists), -P: directory prefix
        cmd = f"wget -nc -P {data_root} {url}"
        exit_code = os.system(cmd)
        if exit_code == 0:
            print("Download successful.")
        else:
            print("Download failed. Check internet connection or url.")
    else:
        print("CIFAR-10 dataset already exists.")

def download_glove_embeddings(data_root='../data', dim=50):
    """
    Downloads GloVe embeddings manually via wget to bypass 
    compute node firewall restrictions.
    """
    # Create directory if it doesn't exist
    os.makedirs(data_root, exist_ok=True)
    
    filename = f'glove.6B.{dim}d.txt'
    zip_filename = 'glove.6B.zip'
    zip_path = os.path.join(data_root, zip_filename)
    file_path = os.path.join(data_root, filename)
    
    if not os.path.exists(file_path):
        if not os.path.exists(zip_path):
            url = "https://huggingface.co/stanfordnlp/glove/resolve/main/glove.6B.zip"
            cmd = f"wget -nc -P {data_root} {url}"
            exit_code = os.system(cmd)
            if exit_code == 0:
                print("GloVe download successful.")
            else:
                print("GloVe download failed. Check internet connection or url.")
        
        # Unzip the file
        if os.path.exists(zip_path):
            print("Extracting GloVe embeddings...")
            os.system(f"unzip -o {zip_path} -d {data_root}")
    else:
        print("GloVe embeddings already exist.")

def download_haarcascade(data_root='../data'):
    """
    Downloads the OpenCV Haar Cascade XML for face detection.
    """
    os.makedirs(data_root, exist_ok=True)
    xml_path = os.path.join(data_root, 'haarcascade_frontalface_default.xml')
    
    if not os.path.exists(xml_path):
        print("Downloading Haar Cascade XML...")
        url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
        cmd = f"wget -nc -P {data_root} {url}"
        os.system(cmd)
        print("Download successful.")
    else:
        print("Haar Cascade XML already exists.")