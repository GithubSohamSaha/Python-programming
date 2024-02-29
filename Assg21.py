def count_word_letter_occurrences(text):
    # Count word occurrences using dictionary
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # Count letter occurrences using dictionary
    letter_count = {}
    for char in text:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return word_count, letter_count
def invert_dictionary(input_dict):
    inverted_dict = {value: key for key, value in input_dict.items()}
    return inverted_dict
# Example text (replace with your own text)
text = "This is a long string of text. This text will be used to count word and letter occurrences."
# Count word and letter occurrences
word_occurrences, letter_occurrences = count_word_letter_occurrences(text)
print("Word occurrences:")
print(word_occurrences)
print("\nLetter occurrences:")
print(letter_occurrences)
# Example dictionary (replace with your own dictionary)
initial_dict = {1: 'a', 2: 'b', 3: 120}
# Invert the dictionary
inverted_dict = invert_dictionary(initial_dict)
print("\nInverted dictionary:")
print(inverted_dict)
