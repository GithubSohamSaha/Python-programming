# 6. CSV File Reader and Writer
# •Problem: Write a program to read data from a CSV file, modify the data, and write it to another CSV file.
# •Example: Given a CSV file containing user information, modify one of the fields (e.g., change email addresses) and save the changes to a new CSV file.
# •Objective: Work with CSV files, reading and writing data using Python’s csv module.

import csv

def modify_csv(input_file, output_file, field_to_modify, modify_function):
    try:
        # Read the data from the input CSV file
        with open(input_file, 'r', newline='') as infile:
            reader = csv.DictReader(infile)
            rows = list(reader)  # Store all rows in a list
            fieldnames = reader.fieldnames  # Get field names (headers)

        # Check if the field to modify exists
        if field_to_modify not in fieldnames:
            print(f"Error: Field '{field_to_modify}' not found in the CSV file.")
            return

        # Modify the specified field using the provided function
        for row in rows:
            row[field_to_modify] = modify_function(row[field_to_modify])

        # Write the modified data to the output CSV file
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the header
            writer.writerows(rows)  # Write the modified rows

        print(f"CSV file modified successfully and saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example modify function to change email addresses
def modify_email(email):
    if '@' in email:
        username, domain = email.split('@')
        return f"{username}@newdomain.com"  # Change domain
    return email

# File paths
input_file = 'users.csv'  # Input CSV file
output_file = 'updated_users.csv'  # Output CSV file

# Field to modify
field_to_modify = 'Email'

# Modify the CSV file
modify_csv(input_file, output_file, field_to_modify, modify_email)
