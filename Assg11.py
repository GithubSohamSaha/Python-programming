# Function to convert decimal to binary using recursion
def decimal_to_binary(decimal_num, recursion_limit=0):
    print(decimal_num % 2, end='')
    if decimal_num > 1:
        decimal_to_binary(decimal_num // 2, recursion_limit + 1)
    else:
        print("\nRecursion stack size:", recursion_limit)
    

# Taking user input for the decimal number
decimal_number = int(input("Enter a decimal number: "))


# Calling the function with named arguments
decimal_to_binary(decimal_num=decimal_number)

