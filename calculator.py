# This is a calculator application
print("Welcome! This is a calculator.")

while True:
    try:
        first_number = float(input("Enter the first number: "))
        break
    except ValueError:
        print("That's not a valid number. Try again.")

while True:
    try:
        second_number = float(input("Enter the second number: "))
        break
    except ValueError:
        print("That's not a valid number. Try again.")

result = 0.0

print("Select an operation:\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division")
while True:
    try:
        operation = int(input(">> "))
        if operation == 1:
            result = first_number + second_number
            break
        elif operation == 2:
            result = first_number - second_number
            break
        elif operation == 3:
            result = first_number * second_number
            break
        elif operation == 4:
            if second_number == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = first_number / second_number
            break
        else:
            print("Invalid input. Choose a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print("The result is:", result)
print("Goodbye!")
