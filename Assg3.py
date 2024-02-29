a=int(input("The Co-efficient of x^2: "))
b=int(input("The Co-efficient of x: "))
c=int(input("The constant term :"))

discriminant = (b**2) - (4*a*c)  

root1 = (-b-(discriminant**0.5))/(2*a) 
root2 = (-b+(discriminant**0.5))/(2*a)

print("The roots of the quadratic equation {0}x^2 + {1}x + {2} is {3} and {4}".format(a,b,c,root1,root2))



