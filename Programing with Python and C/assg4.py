# 4. File Comparison
# •Problem: Write a Python program to compare two text files and highlight the differences between them. 
# •Example: Compare file1.txt and file2.txt line by line and print the differences. 
# •Objective: Read both files, compare their contents, and identify the differences (line by line or word by word).

from difflib import Differ

# Function to compare two files line by line
def compare_files(file1, file2):
    try:
        # Open both files in read mode
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            # Read all lines from both files
            lines1 = f1.readlines()
            lines2 = f2.readlines()

        print(f"Comparing '{file1}' and '{file2}':\n")

        # Get the maximum number of lines from both files
        max_lines = max(len(lines1), len(lines2))

        # Compare files line by line
        print("Line-by-Line Comparison:\n")
        for i in range(max_lines):
            # Get lines from each file, defaulting to an empty string if the line doesn't exist
            line1 = lines1[i].strip() if i < len(lines1) else "(no line)"
            line2 = lines2[i].strip() if i < len(lines2) else "(no line)"

            # Highlight differences
            if line1 != line2:
                print(f"Line {i + 1}:")
                print(f"  File 1: {line1}")
                print(f"  File 2: {line2}")
                print()
        
        # Word-by-word comparison for differing lines
        print("\nWord-by-Word Comparison (for differing lines):\n")
        differ = Differ()
        for i in range(max_lines):
            line1 = lines1[i].strip() if i < len(lines1) else ""
            line2 = lines2[i].strip() if i < len(lines2) else ""
            if line1 != line2:
                print(f"Line {i + 1}:")
                diff = list(differ.compare(line1.split(), line2.split()))
                for word in diff:
                    if word.startswith('- '):
                        print(f"  Missing in File 2: {word[2:]}")
                    elif word.startswith('+ '):
                        print(f"  Missing in File 1: {word[2:]}")
                    elif word.startswith('? '):
                        pass  # Ignore alignment markers
                    else:
                        print(f"  Common: {word[2:]}")
                print()
        print("Comparison complete.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

# File names to compare
file1 = 'assg4_file1.txt'
file2 = 'assg4_file2.txt'

# Compare the files
compare_files(file1, file2)
