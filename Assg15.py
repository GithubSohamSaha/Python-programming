import sys
def read_first_last_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if n > len(lines):
                n = len(lines)
            print(f"First {n} lines:")
            for i in range(n):
                print(lines[i].strip())
            print(f"\nLast {n} lines:")
            for i in range(-n, 0):
                print(lines[i].strip())
    except FileNotFoundError: # Handle the FileNotFoundError if the specified file doesn't exist
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
# Check if the number of command line arguments is not equal to 3
if len(sys.argv) != 3:
    print("Usage: python script.py <file_name> <n>")
else:
    file_name = sys.argv[1]
    try:
        n = int(sys.argv[2])
        if n <= 0:
            print("Error: Please provide a positive value for n.")
        else:
            read_first_last_n_lines(file_name, n)
    except ValueError:
        print("Error: Please provide a valid integer value for n.")
