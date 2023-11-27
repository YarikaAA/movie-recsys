import requests
import os
import zipfile

def download_and_unpack_movielens(url, target_folder):
    """
    Download and unpack the MovieLens 100K dataset.

    : param url: URL of the MovieLens 100K dataset
    : param target_folder: Folder where the dataset will be saved
    """
    os.makedirs(target_folder, exist_ok=True)
    target_zip_path = os.path.join(target_folder, 'movielens-100k.zip')

    # Download the file
    response = requests.get(url)
    response.raise_for_status()

    # Save the file
    with open(target_zip_path, 'wb') as file:
        file.write(response.content)

    print(f"File downloaded and saved to {target_zip_path}")

    # Unpack the zip file
    with zipfile.ZipFile(target_zip_path, 'r') as zip_ref:
        zip_ref.extractall(target_folder)
    
    print(f"File unpacked in {target_folder}")

dataset_url = "http://files.grouplens.org/datasets/movielens/ml-100k.zip"
target_folder = "../data/raw/"

download_and_unpack_movielens(dataset_url, target_folder)
