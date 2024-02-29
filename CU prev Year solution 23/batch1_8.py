class Length:
    def __init__(self, feet=0, inches=0):
        self.feet = feet
        self.inches = inches

    def setLength(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def getLength(self):
        return self.feet, self.inches

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"

    def __add__(self, other):
        total_feet = self.feet + other.feet
        total_inches = self.inches + other.inches

        if total_inches >= 12:
            total_feet += total_inches // 12
            total_inches %= 12

        return Length(total_feet, total_inches)

# Example usage
length1 = Length(3, 6)
length2 = Length(2, 9)

print("Length 1:", length1)
print("Length 2:", length2)

print("\nAdding lengths:")
total_length = length1 + length2
print("Total length:", total_length)
