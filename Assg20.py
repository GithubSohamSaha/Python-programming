def deduplicate_list(input_list):
    #set() for removing duplicates and preserve unique elements
    unique_numbers = set(input_list)
    return unique_numbers
def deduplicate_string(input_string):
    # Convert the string to a set to remove duplicate characters
    unique_characters = set(input_string)
    return unique_characters
def jaccard_similarity(set1, set2):
    # Jaccard similarity: Intersection / Union
    jaccard_sim = len(set1.intersection(set2)) / len(set1.union(set2))
    return jaccard_sim
def cosine_similarity(set1, set2):
    # Cosine similarity: Intersection / (sqrt(len(set1)) * sqrt(len(set2)))
    cosine_sim = len(set1.intersection(set2)) / (len(set1) ** 0.5 * len(set2) ** 0.5)
    return cosine_sim
# Example list and string (replace with your own data)
numbers = [1, 2, 3, 2, 4, 5, 3, 6, 9]
text = "hellohelloMisterWorld"
# Deduplicate list and string
unique_numbers = deduplicate_list(numbers)
unique_characters = deduplicate_string(text)
print(f"Unique numbers: {unique_numbers}")
print(f"Unique characters: {unique_characters}")
# Example sets for similarity calculations (replace with your own sets)
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
# Calculate Jaccard similarity
jaccard = jaccard_similarity(set1, set2)
print(f"Jaccard similarity: {jaccard}")
# Calculate Cosine similarity
cosine = cosine_similarity(set1, set2)
print(f"Cosine similarity: {cosine}")
