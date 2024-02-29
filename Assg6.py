# Function to calculate the Gaussian addition
def gaussian_addition(input_list):
    length = len(input_list)

    # Ensure the list has an even number of elements
    if length % 2 != 0:
        print("List must have an even number of elements.")
        return

    # Initialize variables for the result and the index
    result = 0
    left = 0
    right = length - 1

    while left < right:
        partial_sum = input_list[left] + input_list[right]
        print("{0} + {1} = {2}".format(input_list[left],input_list[right],partial_sum))
        result += partial_sum
        left += 1
        right -= 1

    print("Result:", result)

# Input a list using the range function
input_list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(0,n):
    element=int(input())
    input_list.append(element)


# Call the Gaussian addition function
gaussian_addition(input_list)
