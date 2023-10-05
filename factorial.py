#WAP in python to calculate the factorial of a given number

number=int(input("Enter the number :"))
factorial=1
#Calculation the factorial using for loop
for i in range(1,number+1):
    factorial=factorial*i
    
print("The factorial of {0} is {1}".format(number, factorial))

"""
In the above program the calculation of factorial is going like this 1*2*3=6(Ascending order)

if we want to calculate like 3*2*1=6

we can do this
for i in (number,1,-1):
    .........

"""