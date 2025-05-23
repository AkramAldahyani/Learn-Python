# This is a guessing app
# Features to add
# 1- After the game ends, ask the user if they want to play again. ✅
# 2- Let the user choose a difficulty (Easy, Medium, Hard).
# 3- If the user enters a number outside the allowed range, remind them of the valid range.


import random

counter = 0
secret_number = random.randint(1, 10)
while True:
    counter += 1
    if counter == 5:
        print(f"Game over! The number you were looking for was: {str(secret_number)}\n")
        break
    try:
        number = int(input("Please enter a number between 1 and 10: "))
        if number > secret_number:
            print("You guessed too high.\n")
        elif number < secret_number:
            print("You guessed too low.\n")
        elif number == secret_number:
            print("You guessed the correct number.\n")
            on = input("Would you like to play again? (y/n): ")
            if on.lower() == "y":
                counter = 0
                continue
            elif on.lower() == "n":
                print("Thank you for playing!")
                break
    except ValueError:
        print("Invalid choice. Please enter a number between 1-10.\n")
