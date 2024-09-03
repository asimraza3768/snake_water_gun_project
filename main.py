import random

# making list

options = ["snake", "water", "gun"]


again = True
while (again == True):
    # taking the random choice of computer and user
    computer_choice = random.choice(options)
    print(options)
    user_choice = input("Enter your choice: ").lower().replace(" ","")

    if user_choice not in options:
        print("Invalid input! Please enter 'snake', 'water', or 'gun'.")
        continue

    if (computer_choice == "snake" and user_choice == "water"):
        print("The snake wins by drinking the water.")
    elif (computer_choice == "snake" and user_choice == "gun"):
        print("The gun kills the snake and wins.")
    elif (computer_choice == "snake" and user_choice == "snake"):
        print("Tie - Both chose Snake")
    elif (computer_choice == "water" and user_choice == "snake"):
        print("Snake wins - Snake drowns water")
    elif (computer_choice == "water" and user_choice == "water"):
        print("Tie - Both chose water")
    elif (computer_choice == "water" and user_choice == "gun"):
        print("water wins - water extinguishes gun")
    elif (computer_choice == "gun" and user_choice == "snake"):
        print("gun wins - gun shoots snake")
    elif (computer_choice == "gun" and user_choice == "water"):
        print("water wins - water extinguishes gun")
    elif (computer_choice == "gun" and user_choice == "gun"):
        print("Tie - Both chose gun")

    # Asking user to play again 
    try_again = input("You wanna play again (y/n): ")
    try_again = try_again.lower().strip()
    if try_again =="y":
        again =True
    elif try_again =="n":
        again = False
    else:
        print("Invalid response! Exiting game.")    
        print("It was very nice playing!")
        break


    
    