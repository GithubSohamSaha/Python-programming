# Create a list
fruits = ['Apple', 'Banana', 'Mango']
print(f"the original list of friut is: {fruits}")
modified_fruits = fruits
# Add an element 'Guava' to the end of the list
modified_fruits.append('Guava')
print("List after adding guava at last: ",modified_fruits)
# Change 'Mango' to 'Pomegranate'
if 'Mango' in modified_fruits:
    index = modified_fruits.index('Mango')
    modified_fruits[index] = 'Pomegranate'
print("List after changing the mango to pomogranate: ",modified_fruits)
# Delete the element 'Banana' if it exists
if 'Banana' in modified_fruits:
    modified_fruits.remove('Banana')
print("List after deleting the banana: ",modified_fruits)
# Check if 'Mango' exists in the list
mango_exists = mango_exists = any("Mango" in fruit for fruit in modified_fruits)
print("Result of checking if mango exist in the list: ", mango_exists)