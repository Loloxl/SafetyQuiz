import random
def awnsercheck():
    if awnser1=="B":
        score==score+1
        print("You got it right!")
    else:
        print("You got it wrong!")

name = input("\nWhat is your name?")
score = 0
questions = {"Some one you don't know asks for your password, what do you do?":
                 {"A:": "Give it to them",
                  "B:": "Block them",
                  "C:": "Politely decline"},
             "A stranger asks for pictures for you in an online chatroom,what do you do?":
                 {"A:": "Block them",
                  "B:": "Flipping send it",
                  "C:": "Tell them your ugly", },
             "A guy you have know online for 3 months but never seen asks you to meet up,what do you do":
                 {"A:": "Ask him for a picture",
                  "B:": "Meet up with him",
                  "C:": "Ask your parents if you can trust him"},
             "Your friend wants you to join this shady website that gives out free games,what do you do?":
                 {"A:": "Join!",
                  "B:": "Tell him to join this other one you found",
                  "C:": "Politely decline and say you dont trust that website"},
             "You get an ad for a free phone,it says you have to click on it,what do you do":
            {"A:": "Click on the ad",
             "B:": "Close the website",
             "C:": "Explore the website"}}


for x in questions.keys():
    print(x, "\n", questions[x])
    awnser1=input("Enter your anwser")
    awnsercheck()


#def ask(question_num):
