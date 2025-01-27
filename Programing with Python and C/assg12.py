# 12. Finding Duplicate Files in a Directory
# •Problem: Write a program to scan a directory and identify duplicate files based on file content (not file names).
# •Example: Compare all files in a given directory and identify any files that have the same content.
# •Objective: Use hashing or byte-by-byte comparison to identify duplicate files in a directory.

import os
import hashlib
def hash_file(file_path):
    """Generate a hash for the file content using SHA-256."""
    hash_obj = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):  # Read the file in chunks to handle large files
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except Exception as e:
        print(f"Error hashing file {file_path}: {e}")
        return None

def find_duplicate_files(directory):
    """Find duplicate files in the given directory based on content."""
    file_hashes = {}  # Dictionary to store hash: file paths
    duplicates = []  # List to store duplicate file pairs

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            if file_hash:
                if file_hash in file_hashes:
                    duplicates.append((file_hashes[file_hash], file_path))
                else:
                    file_hashes[file_hash] = file_path
    return duplicates

def display_duplicates(duplicates):
    """Display duplicate file information."""
    if duplicates:
        print("Duplicate files found:")
        for original, duplicate in duplicates:
            print(f"Original: {original}")
            print(f"Duplicate: {duplicate}\n")
    else:
        print("No duplicate files found.")
# Directory to scan
directory = input("Enter the directory to scan for duplicates: ")

# Find and display duplicate files
duplicates = find_duplicate_files(directory)
display_duplicates(duplicates)
