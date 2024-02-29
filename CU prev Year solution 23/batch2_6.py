def number_of_factors(val):
    # Check if input is positive
    if val <= 0:
        print("Input must be a positive integer.")
        return None

    # Initialize a list to store factors
    factors = []

    # Find factors of the number
    for i in range(1, val + 1):
        if val % i == 0:
            factors.append(i)

    return factors

def list_of_factors(val):
    # Check if input is positive
    if val <= 0:
        print("Input must be a positive integer.")
        return None

    # Initialize a count to store the number of factors
    count = 0

    # Count factors of the number
    for i in range(1, val + 1):
        if val % i == 0:
            count += 1

    return count

# Example usage:
num = 12
print(f"Factors of {num}: {number_of_factors(num)}")
print(f"Number of factors of {num}: {list_of_factors(num)}")
