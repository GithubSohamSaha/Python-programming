def convert_case(name):
    converted_name = ""
    for char in name:
        if char.isupper():
            converted_name += char.lower()
        elif char.islower():
            converted_name += char.upper()
        else:
            converted_name += char
    return converted_name

# Example usage:
name = input("Enter a name: ")
converted_name = convert_case(name)
print("Converted name:", converted_name)
