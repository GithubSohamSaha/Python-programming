# 7. Parsing JSON Files
# •Problem: Write a program to read a JSON file, parse the data, and print it in a human-readable format.
# •Example: Given a JSON file with nested structures, extract specific pieces of data (e.g., user details) and display them.
# •Objective: Read and parse JSON files using Python’s json module and extract specific data fields.

import json

def parse_json_file(json_file, fields_to_extract=None):
    try:
        # Open and read the JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)  # Parse JSON into a Python dictionary or list

        # Print the JSON data in a human-readable format
        print("Full JSON Data (Formatted):")
        print(json.dumps(data, indent=4))  # Pretty print JSON

        # Extract and print specific fields if requested
        if fields_to_extract:
            print("\nExtracted Data:")
            for field in fields_to_extract:
                extracted_value = extract_field(data, field)
                print(f"{field}: {extracted_value if extracted_value else 'Field not found'}")
        else:
            print("\nNo specific fields to extract.")
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    except Exception as e:
        print(f"An error occurred: {e}")

def extract_field(data, field):
    # Recursively extract data from nested JSON structures
    keys = field.split('.')  # Support nested fields with dot notation
    value = data
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return None  # Field not found
    return value

# File path
json_file = 'data.json'

# Fields to extract (supports dot notation for nested fields)
fields_to_extract = ['user.name', 'user.email', 'user.details.age']

# Parse and process the JSON file
parse_json_file(json_file, fields_to_extract)
