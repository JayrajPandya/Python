import random

while True:
    selection = ["rock","paper","scissors"]

    computer = random.choice(selection)
    player = None

    while player not in selection:
        player = input("rock, paper, or scissors?:").lower()
        print("")
    if player == computer:
        print("player: ",player)
        print("computer: ", computer)
        print("It's a Tie!")

    elif player == "rock":
        if computer == "paper":
            print("player: ",player)
            print("computer: ", computer)
            print("You lose!")
        if computer == "scissors":
            print("player: ",player)
            print("computer: ", computer)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("player: ",player)
            print("computer: ", computer)
            print("You lose!")
        if computer == "paper":
            print("player: ",player)
            print("computer: ", computer)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("player: ",player)
            print("computer: ", computer)
            print("You lose!")
        if computer == "rock":
            print("player: ",player)
            print("computer: ", computer)
            print("You win!")

    play_again = input("\nWanna play again? (yes/no): ").lower()
    print("")

    if play_again == "no":
        break

print("Thank you and Have a nice day!")