import os
import hashlib
import json

# Folder where your files are
FOLDER = "my_files"
# This file will store the original file fingerprints
BASELINE = "hashes.json"

# Function to get fingerprint of a file
def get_file_hash(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as file:
        h.update(file.read())
    return h.hexdigest()

# Function to save original fingerprints
def save_baseline():
    files = os.listdir(FOLDER)
    hashes = {}
    for file in files:
        full_path = os.path.join(FOLDER, file)
        if os.path.isfile(full_path):
            hashes[file] = get_file_hash(full_path)
    with open(BASELINE, "w") as f:
        json.dump(hashes, f)
    print("Baseline saved! Run this again to check for changes.")

# Function to compare fingerprints
def check_integrity():
    with open(BASELINE, "r") as f:
        old_hashes = json.load(f)

    current_files = os.listdir(FOLDER)
    new_hashes = {}

    for file in current_files:
        full_path = os.path.join(FOLDER, file)
        if os.path.isfile(full_path):
            new_hashes[file] = get_file_hash(full_path)

    for file in old_hashes:
        if file not in new_hashes:
            print(f"❌ Deleted file: {file}")
        elif old_hashes[file] != new_hashes[file]:
            print(f"⚠️ Modified file: {file}")

    for file in new_hashes:
        if file not in old_hashes:
            print(f"🆕 New file added: {file}")

# Run the right function
if not os.path.exists(BASELINE):
    save_baseline()
else:
    check_integrity()
