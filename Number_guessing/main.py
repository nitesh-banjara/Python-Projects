import random


computer_number = random.randint(1, 100)


max_attempts = 8
attempts = 0

print("Number Guessing Game")
print("Guess a number between 1 and 100.")
print(f"You have {max_attempts} attempts.\n")

while attempts < max_attempts:

    user_choice = int(input("Enter your guess: "))
    attempts += 1

    if user_choice == computer_number:
        print("\nCorrect!")
        print(f"You guessed the number in {attempts} attempts.")
        break

    elif user_choice > computer_number:
        print("Too high. Try a lower number.")

    else:
        print("Too low. Try a higher number.")

    remaining = max_attempts - attempts

    if remaining > 0:
        print(f"Attempts remaining: {remaining}\n")

else:
    print("\nGame Over.")
    print(f"You used all {max_attempts} attempts.")
    print(f"The correct number was: {computer_number}")