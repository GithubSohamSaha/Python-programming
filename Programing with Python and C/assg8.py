# 8. Binary File Reader and Writer
# •Problem: Write a program to read binary data from a file, manipulate it, and write the modified data back to a new file.
# •Example: Read a binary image file, modify some of the pixel values, and save it as a new image.
# •Objective: Work with binary files using Python’s file I/O methods like rb and wb modes.

def read_modify_write_binary(input_file, output_file, modify_function):
    try:
        # Open the input file in binary read mode
        with open(input_file, 'rb') as infile:
            binary_data = infile.read()  # Read the binary data

        # Modify the binary data using the provided function
        modified_data = modify_function(binary_data)

        # Write the modified binary data to the output file
        with open(output_file, 'wb') as outfile:
            outfile.write(modified_data)

        print(f"Binary file '{input_file}' has been processed and saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example modify function to invert binary data (e.g., invert pixel values)
def invert_binary_data(data):
    # Invert each byte using bitwise NOT (~)
    return bytes(~byte & 0xFF for byte in data)

# File paths
input_file = 'D:\sohamsaha\Documents\sohamsaha\B.Tech CSE\CSE SEM-3\Programing with Python and C\input_image.jpg'  # Replace with your binary file path
output_file = 'output_image.jpg'  # Replace with your desired output file path

# Process the binary file
read_modify_write_binary(input_file, output_file, invert_binary_data)
