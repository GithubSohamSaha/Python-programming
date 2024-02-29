def hcf_recursive(a, b):
    if b == 0:
        return a
    else:
        return hcf_recursive(b, a % b)

try:
    intlist = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
    if len(intlist) < 5:
        raise ValueError("List should have at least 5 elements.")

    first_element = intlist[0]
    fifth_element = intlist[4]

    hcf = hcf_recursive(first_element, fifth_element)
    print(f"The HCF of the first and fifth elements ({first_element} and {fifth_element}) is: {hcf}")

except NameError:
    print("Name Error: Variable not found.")
except IndexError:
    print("Index Error: Index out of range.")
except ZeroDivisionError:
    print("Zero Division Error: Cannot divide by zero.")
except ValueError as ve:
    print(f"Value Error: {ve}")
