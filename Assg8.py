# Take two strings from the user

# Write a Python program to take two strings from the user, print a new string where the first
# string is reversed, and the second string is converted to uppercase. Sample strings:
# “Pets“, “party”, output: “steP PARTY”. Only use string slicing and + operators.
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Reverse the first string using string slicing
reversed_string1 = string1[::-1]

# Convert the second string to uppercase
uppercase_string2 = string2.upper()

# Combine the reversed first string and the uppercase second string
result = reversed_string1 + " " + uppercase_string2

# Print the result
print("Output:", result)