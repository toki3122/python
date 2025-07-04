def new_game():
    guesses=[]
    correct_guesses=0
    q_num=1
    for key in questions.keys():
        print("")
        print(key)
        for i in options[q_num-1]:
            print(i)
        guess=input("enter A,B,C or D: ")
        guess=guess.upper()
        guesses.append(guess)
        correct_guesses+=check_answer(questions.get(key),guess)
        q_num+=1
    display_score(correct_guesses,guesses)
def check_answer(answer,guess):
    if answer==guess:
        print("correct!")
        return 1
    else:
        print("wrong!!")
        return 0
def display_score(correct_guesses,guesses):
    print("=====================")
    print("RESULTS")
    print("=====================")
    print("ANSWERS: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("GUESSES: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()
    score=int((correct_guesses/len(questions))*100)
    print("your score is: "+str(score)+"%")
def play_again():
    response=input("would you like to continue?(y/n): ")
    response=response.upper()
    if response=="Y":
        return True
    else:
        return False

questions={
    "who created python?: ":"A",
    "what year was python created?: ":"B",
    "python was tributed to which comedy group?: ":"C",
    "is the earth round?: ":"B"
}
options=[
    ["A. Guido Van Rossum","B. Elon Musk","C. Bill Gates","D.Mark Zuckerberg"],
    ["A. 1989","B. 1991","C. 2000","D. 2016"],
    ["A. Lonely Island","B. Smosh", "C.Monty Python", "SNL"],
    ["A. true","B. false","C. sometimes","D. what's earth"]
]
new_game()
while play_again():
    new_game()
print("bye")