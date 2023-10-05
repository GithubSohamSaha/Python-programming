#WAP a python to calculate the sum of series
#1+x+x^2+x^3+..........+x^n

num=int(input("Enter the n (Nth power): "))
x=int(input("Enter the base:"))
s=0
n1=1
for i in range(0,num+1):
    s+=n1
    n1*=x
print("The result is :",s)