# 11. Counting Lines, Words, and Characters in a File
# •Problem: Write a program to count the number of lines, words, and characters in a text file.
# •Example: Given a text file, calculate the number of lines, words, and characters, and print the results.
# •Objective: Read the file and perform basic text analysis to count lines, words, and characters.

def count_file_content(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            lines = file.readlines()  # Read all lines
            lines = [line for line in lines if line.strip()] # Remove empty lines
        # Count the number of lines
        line_count = len(lines)

        # Count the number of words and characters
        word_count = 0
        char_count = 0

        for line in lines:
            words = line.split()  # Split the line into words
            word_count += len(words)  # Add word count of this line
            char_count += len(line)  # Add character count of this line

        # Print the results
        print(f"File: {file_path}")
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters: {char_count}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File path
file_path = 'example.txt'  # Replace with your text file's path

# Count lines, words, and characters in the file
count_file_content(file_path)
