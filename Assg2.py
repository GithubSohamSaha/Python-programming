number=int(input("Enter the number: "))
temp = number
sum = 0
factorial = 1
length = len(str(number))

       
#this is the part where armstrong checking is done... 
while(temp > 0):
      digit = temp% 10
      sum = sum + digit ** length
      temp //= 10
if number==sum:
        print("The number {0} is an Armstrong number".format(number))
else:
        print("The number {0} is not an Armstrong number".format(number))

#this is the part where factorial is done...        
if number < 0:
        print("Error!!!!!Please enter a positive number")
elif number == 0:
        print("The Factorial of {0} is 1".format(number))
else:   
    for i in range(1,number+1):
        factorial *= i  
print("The Factorial of {0} is {1}".format(number,factorial))
      