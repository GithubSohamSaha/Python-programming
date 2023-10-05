num=int(input("Enter the number of terms should be printed (nth term):"))
f1, f2=0, 1
if num<0:
    print("Enter a positive number of terms!!!!!!!!")
else:
    print("Fibonacci series upto {0}th term is:".format(num))
    print(f1,f2, end=" ")
    for i in range(2,num):
        f3=f1+f2
        f1=f2
        f2=f3
        print(f3, end=" ") 
