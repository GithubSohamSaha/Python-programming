# 2. Count Word Frequency in a Text File
# •Problem: Write a Python program to read a text file and calculate the frequency of each word in the file. 
# •Example: Given a text file, count how many times each word appears and display the results in descending order of frequency. 
# •Objective: Read file contents, split the text into words, and count word frequencies using dictionaries.
from collections import Counter

# Open the input file in read mode
with open('input.txt', 'r') as file:
    # Read the contents of the file
    text = file.read()

# Split the text into words (removing punctuation and converting to lowercase)
words = text.lower().split()

# Use Counter to count the frequency of each word
word_counts = Counter(words)

# Sort the words by frequency in descending order
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Display the word frequencies
print("Word Frequencies (Descending Order):")
for word, count in sorted_word_counts:
    print(f"{word}: {count}")
