#!/usr/bin/env python3

# quit the program when press q
def quit(press):
    if press =="q":
        exit()
        
# check the answer and repeat the question if it neither yes or no
def check(a, q):
    while "python is great":
        if a.lower().strip() == "yes" or a.lower().strip() == "no":
            break
        else:
            print("Wrong input! Try again! $100 fine is this happens again!")
            a=input(q)

# questions on what was done to fix the problem
def fix():
    questions=["Did you say sorry? ", "Did you cook her dinner? ", "Did you do all the laundries?", "Did say 'I love you' over 30 times? ", "Did you buy her chocolates? "]
    for x in range(len(questions)):
        answer=input(questions[x])
        quit(answer)
        check(answer, questions[x])
        if answer.lower().strip() == "yes":
           print("Good job! Keep doing the right thing!")
        elif answer.lower().strip() == "no":
           print("OMG! You are screwed!")

# flow chart of questions
def flowChart():
    questions =["Did you do anything wrong? ", "Did she do anything wrong? "]
    answer1 = input(questions[0])
    quit(answer1)
    check(answer1,questions[0])
    if answer1.lower().strip() == "yes":
        print("Oh no... you lose...")
    elif answer1.lower().strip() == "no":
        print("Ok..")
        answer2=input(questions[1])
        quit(answer2)
        check(answer2,questions[1])
        if answer2.lower().strip() == "yes":
            print("Wow...interesting")
            fix()
            print("However...you lose...she's right...")
        elif answer2.lower().strip() == "no":
            print("Emm...let's see...")
            fix()
            print("Anyway...she's right...you lose...")

# welcome info            
def welcome():
        print("Welcome to 'how to win an arguement with your wife' boot camp!!!\nPlease look carefully and answer the following questions with 'yes' or 'no'")
        x = input("Do you want to continue? ")
        quit(x)
        check(x, "Do you want to continue? ")
        if x.lower().strip() == "yes":
            print("Let's begin....")
        elif x.lower().strip() == "no":
            print("Ok, goodbye!")
            exit()

def main():
    welcome()
    questions=["Waiting a minute...are you married?", "Is your wife around this computer screen? "] 
    while "there are 24 hours in a day":
        answer1=input(questions[0])
        quit(answer1)
        check(answer1,questions[0])
        if answer1.lower().strip() == "no":
           print("Ok, have a good day! Bye!")
           break
        answer2=input(questions[1])
        quit(answer2)
        check(answer2,questions[1])
        if answer2.lower().strip() == "yes":
           print("Shut it down! Run!!!")
           break
        else:
            flowChart()
            print("I hope this helps! Goodbye!")
            break
main()
