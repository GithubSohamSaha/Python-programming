import sys
import string
def count_word_frequency(file_name):
    try:
        with open(file_name, 'r') as file:
            words = file.read().lower().split()
            # Removing punctuation from words
            words = [word.strip(string.punctuation) for word in words]
            word_count = {}
            for word in words:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
            print(f"Word frequency in '{file_name}':")
            for word, count in word_count.items():
                print(f"'{word}': {count}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")   
    except Exception as e:
        print(f"An error occurred: {e}")
if len(sys.argv) != 2:
    print("Usage: python script.py <file_name>")
else:
    file_name = sys.argv[1]
    try:
        count_word_frequency(file_name)   
    except ValueError:
        print("Error: Please provide a valid file name.")
