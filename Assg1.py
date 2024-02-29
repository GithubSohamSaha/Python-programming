number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))

def GCD(number1, number2):
    if(number2==0):
        return abs(number1)
    else:
        return GCD(number2, number1%number2)
    
print("The addition : {0} + {1} = {2}".format(number1,number2,(number1+number2)))
if number1>number2:
    print("The substraction : {0} - {1} = {2}".format(number1,number2,(number1-number2)))
else:
    print("The addition : {1} + {0} = {2}".format(number1,number2,(number2-number1)))        
if number1==0:
    print("The dividend must be a non-zero...........")
else:
    print("The division : {0} / {1} = {2}".format(number1,number2,(number1/number2)))    
print("The multiplication: {0} x {1} = {2}".format(number1,number2,(number1*number2)))
print("The GCD of {0} and {1} is {2}".format(number1,number2,GCD(number1,number2)))