import random
choices=["rock","paper","scissors"]
while True:
    computer=random.choice(choices)
    player=None
    while player not in choices:
        player=input("rock, paper, or scissors: ").lower()
    if player==computer:
        print("Computer picked: "+computer)
        print("tie!!")
    elif player=="rock":
        if computer=="paper":
            print("Computer picked: paper")
            print("you lose!!")
        elif computer=="scissors":
            print("Computer picked: scissors")
            print("you win!!")
    elif player=="paper":
        if computer=="scissors":
            print("Computer picked: scissors")
            print("you lose!!")
        elif computer=="rock":
            print("Computer picked: rock")
            print("you win!!")
    elif player=="scissors":
        if computer=="rock":
            print("Computer picked: rock")
            print("you lose!!")
        elif computer=="paper":
            print("Computer picked: paper")
            print("you win!!")
    play_again=input("play again?(y/n): ").lower()
    if play_again!="y":
        break
print("bye!!")