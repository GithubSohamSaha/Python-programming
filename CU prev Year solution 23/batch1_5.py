def main():
    # Input two sets of city names
    s1 = set(input("Enter city names for set 1 separated by spaces: ").split())
    s2 = set(input("Enter city names for set 2 separated by spaces: ").split())

    # Perform operations
    union_set = s1.union(s2)
    intersection_set = s1.intersection(s2)
    symmetric_difference_set = s1.symmetric_difference(s2)

    # Display results
    print("\nResults:")
    print("Union:", union_set)
    print("Intersection:", intersection_set)
    print("Symmetric Difference:", symmetric_difference_set)

    # Display elements of s1 in upper case and s2 in lower case
    print("\nElements of s1 in upper case:")
    for city in s1:
        print(city.upper())

    print("\nElements of s2 in lower case:")
    for city in s2:
        print(city.lower())

main()
