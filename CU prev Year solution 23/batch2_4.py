def words_ending_with_on(text):
    print("Words ending with 'on':")
    words = text.split()
    for word in words:
        if word.endswith("on"):
            print(word)

def words_with_second_and_third_letters_r_and_e(text):
    print("Words with second and third letters 'r' and 'e':")
    words = text.split()
    for word in words:
        if len(word) >= 3 and word[1] == 'r' and word[2] == 'e':
            print(word)

def words_with_no_vowels(text):
    print("Words with no vowels:")
    words = text.split()
    vowels = 'aeiouAEIOU'
    for word in words:
        if all(char not in vowels for char in word):
            print(word)

# Read the content of the file data.txt
with open("Sample1.txt", "r") as file:
    file_content = file.read()

# (a) Words ending with "on"
words_ending_with_on(file_content)

# (b) Words with second and third letters "r" and "e"
words_with_second_and_third_letters_r_and_e(file_content)

# (c) Words with no vowels
words_with_no_vowels(file_content)
