# sum of the series 0+1+2+.....+ upto nth term using for-loop

number=int(input("Enetr the nth term or the range: "))
result=0
series="" #intialize an empty string to store the series
print("The result is as below:-")
for i in range(0,number):
    result=result+i
    series+=str(i) #Append the current value to the series string
    if i<number:
        series+="+" 
print(f"The series is : {series} = "f"{result}")

    