import random
options = ("rock","paper","scissor")

runing = True
while runing :
    computer = random.choice(options)
    player = None
 
    while player not in options : 
        player = input("Enter a choice(Rock,Paper,scissor): ").lower()
        if player not in options :
            print("Invalid Input")
            continue
        print(f"Player : {player}")
        print(f"Computer : {computer}")

    

        if player == computer :
            print("Its Tie ! ")

        elif player == "rock" and computer == "scissor" :
            print("You won !")

        elif player == "paper" and computer == "rock" :
                print("You won !")
        
        elif player == "scissor" and computer == "paper" :
                print("You won !")

        else :
            print("you lose !!😓")

        play_again = input("Play again ? (y/n)")
        if not play_again == "y" :
             runing = False


print("Thanks for Playing")
