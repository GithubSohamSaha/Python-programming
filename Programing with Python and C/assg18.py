# 18. Generating and Writing Large Data Files
# •Problem: Write a program to generate large data files, such as files containing random numbers, text, or CSV data.
# •Example: Generate a file with 10 million random integers and write it to a file.
# •Objective: Use Python to generate large datasets and write them efficiently to disk.

import random
import csv

def generate_large_data_file(filename, rows, data_type="numbers", delimiter=","):
    """
    Generate a large data file containing random data.
    
    Parameters:
        filename (str): Name of the output file.
        rows (int): Number of rows to generate.
        data_type (str): Type of data to generate ("numbers", "text", or "csv").
        delimiter (str): Delimiter for CSV files (default is ',').
    """
    try:
        with open(filename, "w", newline="") as file:
            if data_type == "numbers":
                for _ in range(rows):
                    number = random.randint(1, 10**6)
                    file.write(f"{number}\n")
            
            elif data_type == "text":
                words = ["apple", "banana", "cherry", "date", "elderberry"]
                for _ in range(rows):
                    sentence = " ".join(random.choices(words, k=10))
                    file.write(f"{sentence}\n")
            
            elif data_type == "csv":
                writer = csv.writer(file, delimiter=delimiter)
                headers = ["ID", "Name", "Score"]
                writer.writerow(headers)
                for i in range(1, rows + 1):
                    row = [i, f"Name_{i}", random.randint(0, 100)]
                    writer.writerow(row)
            
            else:
                print("Invalid data type. Please choose 'numbers', 'text', or 'csv'.")
                return
        
        print(f"File '{filename}' with {rows} rows of {data_type} data created successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# User inputs
filename = input("Enter the output file name (e.g., data.txt or data.csv): ")
rows = int(input("Enter the number of rows to generate: "))
data_type = input("Enter the type of data to generate ('numbers', 'text', 'csv'): ").lower()
delimiter = input("Enter a delimiter for CSV files (default is ','): ") or ","

# Generate the file
generate_large_data_file(filename, rows, data_type, delimiter)
