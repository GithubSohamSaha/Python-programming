#WAP to check grade system using if-elif condition

cgpa=float(input("Enter your obtained CGPA(0.1-9.9): "))

if (cgpa>=10.0 and cgpa<=0.0):
    print("You have entered wrong cgpa") 
elif (cgpa<10.0 and cgpa>9.0):
    print("You got A++ grade......")
elif (cgpa<9.0 and cgpa>8.0):
    print("You got A+ grade......")
elif (cgpa<8.0 and cgpa>7.0):
    print("You got A grade......")
elif (cgpa<7.0 and cgpa>6.0):
    print("You got B+ grade......")
elif (cgpa<6.0 and cgpa>5.0):
    print("You got B- grade......")
elif (cgpa<5.0 and cgpa>4.0):
    print("You got C grade......")
elif (cgpa<4.0 and cgpa>3.0):
    print("You got P grade......")
elif (cgpa<3.0 and cgpa>0.0):
    print("You got F grade. You have failed in the examination...")
