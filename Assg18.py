import sys
def copy_file_content(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            dest.write(src.read())
            print(f"Contents of '{source_file}' copied to '{destination_file}'")
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
def concatenate_files(file1, file2, output_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as output:
            content1 = f1.read()
            content2 = f2.read()
            output.write(content1 + content2)
            print(f"Contents of '{file1}' and '{file2}' concatenated and saved to '{output_file}'")
    except FileNotFoundError:
        print("Error: One of the input files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if len(sys.argv) == 4:
    source_file = sys.argv[1]
    destination_file = sys.argv[2]
    copy_file_content(source_file, destination_file)
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]
    concatenate_files(file1, file2, output_file)
else:
    print("Usage: python script.py <source_file> <destination_file> <output_file>")
