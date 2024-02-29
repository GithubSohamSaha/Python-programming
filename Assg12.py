from functools import reduce

# Finding the maximum value in a list using reduce
num_list = [12, 56, 23, 87, 41, 9, 62]
max_value = reduce(lambda x, y: x if x > y else y, num_list)
print("Maximum value in the list:", max_value)

# Calculating the sum of numbers from 1 to 100 using reduce
sum_1_to_100 = reduce(lambda x, y: x + y, range(1, 101))
print("Sum of numbers from 1 to 100:", sum_1_to_100)
