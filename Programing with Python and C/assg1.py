# •Problem: Write a program to read from one text file and write its contents to another file.
# Example: Given a text file input.txt, create a new file output.txt with the same content.
# •Objective: Read from a file, process the data if needed, and write it to a new file.
# Open the input file in read mode
with open('input.txt', 'r') as input_file:
    # Read the contents of the input file
    content = input_file.read()

# Open the output file in write mode
with open('output.txt', 'w') as output_file:
    # Write the content to the output file
    output_file.write(content)

print("Contents of 'input.txt' have been successfully copied to 'output.txt'.")
