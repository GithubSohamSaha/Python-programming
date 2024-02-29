import sys
def count_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if not lines:
                print(f"The file '{file_name}' is empty.")
            else:
                num_lines = len(lines)
                print(f"The file '{file_name}' has {num_lines} lines.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if len(sys.argv) != 2:
    print("Usage: python script.py <file_name>")
else:
    file_name = sys.argv[1]
    try:
        count_lines(file_name)
    except ValueError:
        print("Error: Please provide a valid file name.")
