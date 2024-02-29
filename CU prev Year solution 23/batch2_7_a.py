def find_numbers(l, N):
    # Initialize count of numbers divisible by 7 and ending in 6
    count = 0

    # List to store the numbers
    numbers = []

    # Iterate through the range from l to N (inclusive)
    for num in range(l, N + 1):
        # Check if the number is divisible by 7 and ends with 6
        if num % 7 == 0 and num % 10 == 6:
            numbers.append(num)
            count += 1

    return numbers, count

# Example usage:
l = 1
N = 60
result, count = find_numbers(l, N)
print("List of numbers:", result)
print("Count:", count)
