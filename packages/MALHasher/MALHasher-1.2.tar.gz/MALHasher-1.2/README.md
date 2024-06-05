# MALHasher

`malhasher` is a custom Python package that provides SHA256 and SHA1 hashing functions, and a feature to match generated hash values against a dataset of hash values stored in a CSV file within the package.

## Installation

To install the package, run the following command:

```sh
pip install malhasher
```

## Features

- **SHA256 Hashing**: Generate SHA256 hash values for strings and files.
- **SHA1 Hashing**: Generate SHA1 hash values for strings and files.
- **Hash Matching**: Match generated hash values against a precomputed dataset of hash values stored in a CSV file.


### SHA256 Hashing
Generate SHA256 hash for a given string.
Generate SHA256 hash for a file.

### SHA1 Hashing

Generate SHA1 hash for a given string.
Generate SHA1 hash for a file.

### Hash Matching
Load a dataset of hash values from a CSV file.
Match generated hash values against the dataset of hash values.

## Importing the Package
```sh
from malhasher import sha256, sha1, sha256_file, sha1_file, load_hash_dataset_from_csv, load_hash_dataset_from_package, match_hash
```

## Generate SHA256 Hash for a File
```sh
from malhasher import sha256_file

file_path = "path/to/your/file"
file_hash_value = sha256_file(file_path)
print(f"SHA256 file: {file_hash_value}")
```
### Generate SHA256 Hash for a String

```sh
from malhasher import sha256

data = b"example data"
hash_value = sha256(data)
print(f"SHA256: {hash_value}")
```
## Generate SHA1 Hash for a File

```sh
from malhasher import sha1_file

file_path = "path/to/your/file"
file_hash_value = sha1_file(file_path)
print(f"SHA1 file: {file_hash_value}")
```

### Generate SHA1 Hash for a String

```sh
from malhasher import sha1

data = b"example data"
hash_value = sha1(data)
print(f"SHA1: {hash_value}")

```

## Malware Hash Cheaking Using Defoult Dataset

```sh
import os
from malhasher import sha256_file, sha1_file, load_hash_dataset_from_package, match_hash

def check_file_for_malware(file_path):
    # Generate SHA256 and SHA1 hashes for the file
    sha256_hash = sha256_file(file_path)
    sha1_hash = sha1_file(file_path)

    # Load hash datasets from the package
    sha256_set, sha1_set = load_hash_dataset_from_package()

    # Check if the generated hashes match any in the datasets
    is_malware_sha256 = match_hash(sha256_hash, sha256_set)
    is_malware_sha1 = match_hash(sha1_hash, sha1_set)

    # Determine if the file is malware
    if is_malware_sha256 or is_malware_sha1:
        print(f"The file '{file_path}' is identified as malware.")
    else:
        print(f"The file '{file_path}' is not identified as malware.")

if __name__ == "__main__":
    # Specify the path to the file you want to check
    file_path = 'Your File Path'  # Replace with the actual file path

    if not os.path.isfile(file_path):
        print(f"File '{file_path}' does not exist.")
    else:
        check_file_for_malware(file_path)

```
## Malware Hash Cheaking From External Dataset

```sh
import pandas as pd
import os
from malhasher import sha256_file, sha1_file

def check_file_for_malware(file_path, dataset_path):
    # Read the dataset
    dataset = pd.read_csv(dataset_path)
    
    # Generate SHA256 and SHA1 hashes for the file
    sha256_hash = sha256_file(file_path)
    sha1_hash = sha1_file(file_path)
    
    # Check if the generated hashes match any in the dataset
    match = dataset[(dataset['SHA256'] == sha256_hash) | (dataset['SHA1'] == sha1_hash)]
    
    if not match.empty:
        print(f"The file '{file_path}' is identified as malware.")
        for _, row in match.iterrows():
            print(f"Malware Type: {row['Type']}")
            print(f"Malware Family: {row['Family']}")
            print(f"Malware Size: {row['Size']} bytes")
            print(f"Malware Detections: {row['Detections']}")
            print(f"Malware Sandbox Behavior: {row['Sandbox Behavior']}")
    else:
        print(f"The file '{file_path}' is not identified as malware. Status: Undetectable")

# Example usage
file_path = 'Your File Path'  # Replace with the actual file path
dataset_path = 'YourDataset.csv'  # Replace with the actual dataset path

if os.path.isfile(file_path) and os.path.isfile(dataset_path):
    check_file_for_malware(file_path, dataset_path)
else:
    print("Invalid file path or dataset path.")

```

# Thank Your For Use This Library

