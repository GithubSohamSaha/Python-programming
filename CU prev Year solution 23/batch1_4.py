import sys

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as f_source:
            with open(destination_file, 'w') as f_dest:
                line_number = 1
                for line in f_source:
                    line_length = len(line.strip())  # Length of line excluding whitespace
                    f_dest.write(f"{line_number}: {line.strip()} {line_length}\n")
                    line_number += 1
        print("File copied successfully!")
    except FileNotFoundError:
        print("One or both files not found.")
    except PermissionError:
        print("Permission denied. Please check file permissions.")
    except Exception as e:
        print("An error occurred:", str(e))

if len(sys.argv) != 3:
    print("Usage: python program_name.py source_file destination_file")
    sys.exit(1)

source_file = sys.argv[1]
destination_file = sys.argv[2]

if source_file == destination_file:
    print("Source and destination files should be different.")
    sys.exit(1)

copy_file(source_file, destination_file)
