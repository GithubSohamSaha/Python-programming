def longest_chain_of_zeros(lst):
    max_count = 0
    max_start = -1
    max_end = -1

    current_count = 0
    current_start = -1

    for i in range(len(lst)):
        if lst[i] == 0:
            if current_start == -1:
                current_start = i
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_start = current_start
                max_end = i - 1
            current_count = 0
            current_start = -1

    # Check for the longest chain at the end of the list
    if current_count > max_count:
        max_count = current_count
        max_start = current_start
        max_end = len(lst) - 1

    return max_count, (max_start, max_end)

# Example usage:
lst = [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
longest_zeros_count, span = longest_chain_of_zeros(lst)
print(f"The longest run of zeros is {longest_zeros_count}.")
print(f"Span: {span[0]} to {span[1]}")
