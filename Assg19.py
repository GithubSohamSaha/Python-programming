import pickle
def binarize_and_store(data):
    try:
        with open("myBinarizedData", 'wb') as file:
            binarized_data = pickle.dumps(data)
            file.write(binarized_data)
            print("Data binarized and stored in 'myBinarizedData' file.")
    except Exception as e:
        print(f"An error occurred while binarizing and storing the data: {e}")
def retrieve_and_display():
    try:
        with open("myBinarizedData", 'rb') as file:
            retrieved_data = pickle.load(file)
            print("Retrieved data:")
            print(retrieved_data)
    except FileNotFoundError:
        print("Error: File 'myBinarizedData' not found.")
    except Exception as e:
        print(f"An error occurred while retrieving and displaying the data: {e}")
# Example data (replace this with your data)
data_to_binarize = {'key1': 123, 'key2': [4, 5, 6], 'key3': {'nested_key': 'value'}}
# Binarize and store the data
binarize_and_store(data_to_binarize)
# Retrieve and display the pickled data
retrieve_and_display()
