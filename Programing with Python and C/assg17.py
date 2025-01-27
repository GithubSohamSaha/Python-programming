def find_and_replace(file_path, search_text, replace_text, output_file=None):
    """
    Reads a file, searches for a specific text pattern, and replaces it with another text.
    
    Parameters:
        file_path (str): Path to the input file.
        search_text (str): Text pattern to search for.
        replace_text (str): Text to replace the search pattern with.
        output_file (str): Path to save the modified file. If None, overwrites the original file.
    """
    try:
        # Open and read the original file
        with open(file_path, 'r') as file:
            content = file.read()

        # Perform the search and replace operation
        modified_content = content.replace(search_text, replace_text)

        # Determine the file to save the changes
        save_path = output_file if output_file else file_path

        # Write the modified content to the output file
        with open(save_path, 'w') as file:
            file.write(modified_content)

        print(f"'{search_text}' has been replaced with '{replace_text}' in '{save_path}'.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# User inputs
file_path = input("Enter the path of the file to modify: ")
search_text = input("Enter the text to search for: ")
replace_text = input("Enter the text to replace it with: ")
output_file = input("Enter the output file path (leave blank to overwrite the original file): ")

# Call the function
find_and_replace(file_path, search_text, replace_text, output_file if output_file.strip() else None)
