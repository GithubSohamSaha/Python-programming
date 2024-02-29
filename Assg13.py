# Function to generate the first n Fibonacci numbers
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return fibonacci_sequence

# Generating the first 11 Fibonacci numbers
fibonacci_numbers = generate_fibonacci(11)

# Filtering out odd and even elements separately
odd_numbers = list(filter(lambda x: x % 2 != 0, fibonacci_numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci_numbers))

print("The first 11 Fibonacci numbers:", fibonacci_numbers)
print("Odd Fibonacci numbers:", odd_numbers)
print("Even Fibonacci numbers:", even_numbers)
