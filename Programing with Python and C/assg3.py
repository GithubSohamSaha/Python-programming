# 3. Merging Multiple Text Files into One
# •Problem: Merge the contents of multiple text files into a single file.
# •Example: Given three text files (file1.txt, file2.txt, file3.txt), merge their contents into a new file merged.txt.
# •Objective: Open and read multiple files, then write their contents into a single file.

# List of input files to merge
input_files = ['file1.txt', 'file2.txt', 'file3.txt']

# Name of the output file
output_file = 'merged.txt'

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Loop through each input file
    for file in input_files:
        try:
            # Open the input file in read mode
            with open(file, 'r') as infile:
                # Read and write the content to the output file
                content = infile.read()
                outfile.write(content)
                # Add a newline to separate files (optional)
                outfile.write('\n')
            print(f"Successfully merged {file}")
        except FileNotFoundError:
            print(f"File not found: {file}")

print(f"All files have been merged into {output_file}.")
