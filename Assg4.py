limit = int(input("Enetr the limit (nth term)::"))
a1 = 2
b2 = 1
print("The series is: ")
for i in range(0,limit):
    if (i%2!=0):
        print(b2 ,end=" ")
        b2=b2+2 
    else:
        print(a1 ,end=" ")    
        a1=a1+2
def find_ith_term(i):
    if i % 2 == 0:
        return i - 1
    else:
        return i + 1
i = int(input("\nEnter the value of i to find the i-th term: "))
ith_term = find_ith_term(i)
print("The {}-th term in the series is: {}".format(i, ith_term))
