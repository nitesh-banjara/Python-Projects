import random

item_list = ["snake", "water", "gun"]

while True:
    user_input = input("Choose between snake, water and gun: ").lower()

    if user_input not in item_list:
        print("Please use correct input from snake, water and gun!")
        continue

    comp_input = random.choice(item_list)

    print(f"User choice = {user_input}, \nComputer choice = {comp_input}")

    if user_input == comp_input:
        print("Draw..!")

    elif user_input == "snake":
        if comp_input == "water":
            print("User wins:", user_input)
        else:
            print("Computer wins:", comp_input)

    elif user_input == "gun":
        if comp_input == "snake":
            print("You win!!:", user_input)
        else:
            print("Computer wins!!:", comp_input)

    elif user_input == "water":
        if comp_input == "gun":
            print("You win!!:", user_input)
        else:
            print("Computer wins!!:", comp_input)

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break