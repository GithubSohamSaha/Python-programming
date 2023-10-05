#write a program to swap 2 no. without using 3rd variable
n1=int(input("Enter the 1st number:"))
n2=int(input("Enter the 2nd number:"))
print("Before swaping n1 = {0} and n2 = {1}".format(n1,n2))
n1=n1+n2
n2=n1-n2
n1=n1-n2
print("After swaping  n1 = {0} and n2 = {1}".format(n1,n2))
