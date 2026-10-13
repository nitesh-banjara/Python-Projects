import random

item_list = ["rock", "paper", "scissor"]

while True:
    user_choice = input("Enter your move from Rock, Paper, Scissor: ").lower()

    if user_choice not in item_list:
        print("Please use correct input from Rock, Paper and Scissor!")
        continue

    comp_choice = random.choice(item_list)

    print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

    if user_choice == comp_choice:
        print("Both choose the same: Match Tie!")

    elif user_choice == "rock":
        if comp_choice == "paper":
            print("Computer wins. Paper covers Rock!")
        else:
            print("User wins. Rock smashes Scissor!")

    elif user_choice == "paper":
        if comp_choice == "scissor":
            print("Computer wins. Scissor cuts Paper!")
        else:
            print("User wins. Paper covers Rock!")

    elif user_choice == "scissor":
        if comp_choice == "rock":
            print("Computer wins. Rock smashes Scissor!")
        else:
            print("User wins. Scissor cuts Paper!")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break