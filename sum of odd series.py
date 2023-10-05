#WAP a python to calculate the sum of series
#1+3+5+7+..........+nth term

number=int(input("Enter the nth term: "))
result=0
for i in range(1,number*2,2):
    result=result+i
    
print("The sum the series is: ",result)  