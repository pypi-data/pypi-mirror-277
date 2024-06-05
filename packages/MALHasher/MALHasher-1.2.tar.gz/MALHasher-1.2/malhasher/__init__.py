# mrhashing/__init__.py

from .sha256 import sha256, sha256_file
from .sha1 import sha1, sha1_file
from .CheakHash import load_hash_dataset_from_csv, load_hash_dataset_from_package, match_hash
