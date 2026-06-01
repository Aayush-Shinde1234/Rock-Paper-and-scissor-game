import random
choices = ["Rock","Paper","Scissors"]
player_score = 0
computer_score = 0

print("="*30)
print(" ROCK,PAPER AND SCISSORS GAME")
print("="*30)

play_again = "yes"

while play_again.lower() == "yes":
    #Ask the player for input
    player = ""
    while player not in choices:
         player = input("Enter your choice here : ").capitalize()
    computer = random.choice(choices)

    # shows players score and who wins
    if(player ==  "Rock" and computer == "Paper"):
        print("computer wins")
        computer_score+=1

    elif(player == "Paper" and computer == "Rock"):
        print("You wins")
        player_score+=1

    elif(player == "Scissors" and computer == "Paper"):
        print("You wins")
        player_score+=1

    elif(player == "Paper" and computer == "Scissors"):
        print("Computer wins")
        computer_score+=1

    elif(player == "Scissors" and computer == "Rock"):
        print("Computer wins")
        computer_score+=1

    elif(player == "Rock" and computer == "Scissors"):
        print("You wins")
        player_score+=1

    else:
        print("Its a draw")

    # shows choice and score
    print("Your choice :",player)
    print("Computer choice :",computer)
    print("Score → You:", player_score, "| Computer:", computer_score)
    #Ask to play again
    play_again = input("Do you want to play again? (yes/no): ")

print("Thanks for playing! Final Score → You:", player_score, "| Computer:", computer_score)
