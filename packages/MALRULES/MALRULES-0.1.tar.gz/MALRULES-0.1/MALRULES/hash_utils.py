# MALRULES/hash_utils.py

from malhasher import sha256_file, sha1_file

def generate_file_hashes(file_path):
    sha256_hash = sha256_file(file_path)
    sha1_hash = sha1_file(file_path)
    return sha256_hash, sha1_hash
