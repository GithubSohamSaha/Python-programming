import sys

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect_square(x):
    sqrt_x = int(x ** 0.5)
    return sqrt_x * sqrt_x == x

def is_fibonacci(num):
    return is_perfect_square(5*num*num + 4) or is_perfect_square(5*num*num - 4)

def print_non_prime_non_fibonacci(a, b):
    for num in range(a, b+1):
        if not is_prime(num) and not is_fibonacci(num):
            print(num)

if len(sys.argv) != 3:
    print("Usage: python program_name.py a b")
    sys.exit(1)

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except ValueError:
    print("Please enter valid integer values for a and b.")
    sys.exit(1)

if a >= b:
    print("Please enter a value of a less than b.")
    sys.exit(1)

print_non_prime_non_fibonacci(a, b)
