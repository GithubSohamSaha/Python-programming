
# Input the number of rows you want in the Pascal's triangle
n = int(input("Enter the number of rows for Pascal's triangle: "))
def factorial(n):
    if n == 0 or n ==1 :
        return 1
    else:
        return (n * factorial(n-1))
# Print Pascal's Triangle in Python
for i in range(n):
	for j in range(n-i+1):
		# for left spacing
		print(end=" ")
	for j in range(i+1):
		# nCr = n!/((n-r)!*r!)
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
	# for new line
	print()

