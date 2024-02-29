# Write a Python program to perform the following: From a list of words, join all the words in
# the odd and even indices to form two strings. Use list slicing and join methods.

# List of words
word_list = ["apple", "banana", "orange", "grape", "kiwi", "melon"]

# Get words at odd indices and join them
odd_indices_words = " ".join(word_list[1::2])

# Get words at even indices and join them
even_indices_words = " ".join(word_list[::2])

# Print the results
print("The Original List of words are:", word_list)
print("Words at odd indices:", odd_indices_words)
print("Words at even indices:", even_indices_words)
