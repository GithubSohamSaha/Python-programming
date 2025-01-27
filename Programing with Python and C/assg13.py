# 13. Directory Walker (Recursive File Listing)
# •Problem: Write a Python program to recursively list all files and directories in a given directory.
# •Example: Given a directory, output a tree-like structure of all files and subdirectories within it.
# •Objective: Use os or os.path to traverse directories and print their structure.

import os

def list_directory(directory, indent=0):
    """Recursively list all files and directories in a given directory."""
    try:
        # Get all items in the directory
        items = os.listdir(directory)
    except PermissionError:
        print(" " * indent + f"[Permission Denied]: {directory}")
        return
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        return

    # Sort items to display directories first
    items.sort(key=lambda x: (not os.path.isdir(os.path.join(directory, x)), x.lower()))

    for item in items:
        item_path = os.path.join(directory, item)
        # Print the item with indentation
        if os.path.isdir(item_path):
            print(" " * indent + f"[DIR] {item}")
            # Recursively list subdirectories
            list_directory(item_path, indent + 4)
        else:
            print(" " * indent + f"[FILE] {item}")

# Get the directory path from the user
directory = input("Enter the directory to list: ")

# Start listing
print(f"Listing files and directories in: {directory}")
list_directory(directory)
