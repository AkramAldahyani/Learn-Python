# This is a guessing app
import random

counter = 0
secret_number = random.randint(1, 10)
while True:
    counter += 1
    if counter == 4:
        print(f"Game over! The number you were looking for was: {str(secret_number)}")
        break
    try:
        number = int(input("Please enter a number between 1 and 10: "))
        if number > secret_number:
            print("You guessed too high.\n")
        elif number < secret_number:
            print("You guessed too low.\n")
        elif number == secret_number:
            print("You guessed the correct number.")
            break
    except ValueError:
        print("Invalid choice. Please enter a number between 1-10.")
