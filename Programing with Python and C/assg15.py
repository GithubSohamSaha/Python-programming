import os
import time

def get_file_metadata(directory):
    try:
        # Check if the directory exists
        if not os.path.isdir(directory):
            print("Error: The specified directory does not exist.")
            return

        print(f"\nMetadata for files in directory: {directory}\n")
        print(f"{'File Name':<30} {'Size (Bytes)':<15} {'Creation Date':<25} {'Modification Date':<25}")
        print("-" * 100)

        # Iterate over files in the directory
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            
            # Skip subdirectories
            if os.path.isfile(file_path):
                # Get file metadata
                file_stat = os.stat(file_path)
                file_size = file_stat.st_size
                creation_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file_stat.st_ctime))
                modification_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file_stat.st_mtime))

                # Print metadata
                print(f"{file_name:<30} {file_size:<15} {creation_time:<25} {modification_time:<25}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Input directory path
    directory = input("Enter the directory path: ")
    get_file_metadata(directory)

if __name__ == "__main__":
    main()
