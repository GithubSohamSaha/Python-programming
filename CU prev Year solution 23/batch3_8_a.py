def print_pattern(n):
    # Upper half of the pattern
    for i in range(1, n + 1):
        # Print spaces before the first star
        print(" " * (n - i), end="")

        # Print the first star
        print("*", end="")

        # Print spaces between the first and second stars
        if i > 1:
            print(" " * (2 * (i - 1) - 1), end="")

        # Print the second star (except for the first row)
        if i != 1:
            print("*", end="")
        # Move to the next line
        print()

    # Lower half of the pattern
    for i in range(n - 1, 0, -1):
        # Print spaces before the first star
        print(" " * (n - i), end="")

        # Print the first star
        print("*", end="")

        # Print spaces between the first and second stars
        if i > 1:
            print(" " * (2 * (i - 1) - 1), end="")

        # Print the second star (except for the first row)
        if i != 1:
            print("*", end="")
        
        # Move to the next line
        print()

# Test the function with n = 3
if __name__ == "__main__":
    n = 3
    print_pattern(n)
