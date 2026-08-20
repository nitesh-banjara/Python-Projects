import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move from Rock , Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"user_choice = {user_choice}, Computer choice = {comp_choice}")

if (user_choice == comp_choice):
    print("Both chooses same: = Match Tie")

elif (user_choice == "Rock"):
    if (comp_choice == "Paper") :
        print("Computer  wins.  Paper defended you ....")
    else:
        print("User wins.  Rock break you into pices... ")

elif(user_choice == "Paper"):
    if comp_choice =="Scissor":
        print("Computer wins.  Scissor cuts you down.... ")
    else:
        print("Paper wins. Rock can't tear me...")

elif(user_choice == "Scissor"):
    if comp_choice == "Rock":
        print("Compuer wins.Rock smash Scissor....")
    else:
        print("User wins. Paper cut down in pices....")

