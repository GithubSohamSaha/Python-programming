#WAP to find the given number is evem or odd

number=int(input("Enter the number: "))

#checking the number using if-else condition.....
if (number%2==0):
    print("The number {0} is even...".format(number))
elif number==0:
    print("The number {0} is neither odd,nor even...".format(number))
else:
    print("The number {0} is odd...".format(number))   