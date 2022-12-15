import random

while True:
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    user = input("Select rock, paper or scissors: ").lower()

    if user == computer:
        print("computer: ", computer)
        print("user: ", user)
        print("ITS A TIE!")
    elif user == "rock" and computer == "scissors":
        print("computer: ", computer)
        print("user: ", user)
        print("User wins")
    elif user == "papr" and computer == "rock":
        print("computer: ", computer)
        print("user: ", user)
        print("User wins")
    elif user == "scissors" and computer == "paper":
        print("computer: ", computer)
        print("user: ", user)
        print("User wins")
    else:
        print("computer: ", computer)
        print("user: ", user)
        print("Computer wins")

    play_again = input("Do you want to play again? Yes or no: ").lower()
    if play_again == "no":
        print("Thanks! Bye!")
