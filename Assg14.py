# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Taking user input for temperature and choice of conversion
temperature = float(input("Enter the temperature: "))
conversion_choice = input("Enter 'f' for Fahrenheit to Celsius or 'c' for Celsius to Fahrenheit: ")

if conversion_choice == 'f':
    result = fahrenheit_to_celsius(temperature)
    print(f"{temperature} Fahrenheit is equal to {result:.2f} Celsius.")
elif conversion_choice == 'c':
    result = celsius_to_fahrenheit(temperature)
    print(f"{temperature} Celsius is equal to {result:.2f} Fahrenheit.")
else:
    print("Invalid choice. Please enter 'f' or 'c' for conversion.")
