import csv
import os

def load_hash_dataset_from_package():
    """Load the dataset of hash values included in the package."""
    dataset_path = os.path.join(os.path.dirname(__file__), 'data/MRHASHER_dataset.csv')
    return load_hash_dataset_from_csv(dataset_path)

def load_hash_dataset_from_csv(filepath):
    """Load a dataset of SHA256 and SHA1 hash values from a CSV file."""
    sha256_set = set()
    sha1_set = set()
    with open(filepath, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if len(row) > 0:
                sha256_set.add(row[0].strip())
            if len(row) > 1:
                sha1_set.add(row[1].strip())
    return sha256_set, sha1_set

def match_hash(hash_value, hash_set):
    """Match a generated hash value to the dataset."""
    return hash_value in hash_set
