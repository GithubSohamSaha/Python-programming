# 20. File Permissions Checker
# •Problem: Write a Python program that checks the permissions of files in a directory and identifies files with insecure permissions.
# •Example: Scan a directory and identify files that are world-writable or have other risky permissions.
# •Objective: Use Python’s os and stat modules to check file permissions and highlight any potential security risks.

import os
import stat

def check_file_permissions(directory):
    """
    Check the permissions of files in the given directory and identify insecure permissions.
    
    Parameters:
        directory (str): Path to the directory to scan.
    """
    try:
        print(f"Scanning directory: {directory}\n")
        print(f"{'File Name':<40} {'Permissions':<15} {'Insecure?':<10}")
        print("-" * 65)

        # Walk through files in the directory
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)

                # Get file permissions
                file_stat = os.stat(file_path)
                permissions = stat.filemode(file_stat.st_mode)

                # Check for insecure permissions (world-writable)
                is_insecure = False
                if (file_stat.st_mode & stat.S_IWOTH) != 0:  # World-writable
                    is_insecure = True

                # Check for other risky permissions
                insecure_label = "Yes" if is_insecure else "No"

                print(f"{file:<40} {permissions:<15} {insecure_label:<10}")

        print("\nScan complete.")

    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except PermissionError:
        print("Error: Permission denied while accessing files.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Get user input for the directory to scan
directory = input("Enter the directory to scan for file permissions: ")

# Perform the file permissions check
check_file_permissions(directory)
