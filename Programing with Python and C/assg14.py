# 14. Renaming Files in a Directory
# •Problem: Write a program to rename all files in a directory according to a specific pattern.
# •Example: Rename all .txt files in a directory by adding a prefix like old_ to their names.
# •Objective: Use Python’s os or os.rename() function to batch rename files based on specific criteria.

import os

def rename_files_in_directory(directory, prefix='', suffix='', extension_filter=None):
    """
    Rename files in the given directory by adding a prefix or suffix.
    
    Parameters:
        directory (str): Path to the directory containing files to rename.
        prefix (str): Prefix to add to file names.
        suffix (str): Suffix to add to file names (before the extension).
        extension_filter (str): If specified, only rename files with this extension (e.g., '.txt').
    """
    try:
        # Get a list of all files in the directory
        files = os.listdir(directory)

        for file in files:
            file_path = os.path.join(directory, file)

            # Skip directories
            if not os.path.isfile(file_path):
                continue

            # Filter by file extension if specified
            if extension_filter and not file.endswith(extension_filter):
                continue

            # Extract file name and extension
            file_name, file_ext = os.path.splitext(file)

            # Construct the new file name
            new_file_name = f"{prefix}{file_name}{suffix}{file_ext}"
            new_file_path = os.path.join(directory, new_file_name)

            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed: {file} -> {new_file_name}")

        print("\nRenaming complete!")

    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get user inputs
directory = input("Enter the directory path: ")
prefix = input("Enter a prefix to add (leave blank if not needed): ")
suffix = input("Enter a suffix to add (leave blank if not needed): ")
extension_filter = input("Enter the file extension to filter by (e.g., .txt, leave blank for all files): ")

# Rename files in the directory
rename_files_in_directory(directory, prefix, suffix, extension_filter)
