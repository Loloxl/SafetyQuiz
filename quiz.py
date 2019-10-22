import random
name = input("\nWhat is your name?")
score = 0
questions = {"Some one you don't know asks for your password, what do you do?":
                 {"A:": "Give it to them",
                  "B:": "Block them",
                  "C:": "Politely decline"},
             "2":
                 {"A:": "??"}}

def ask(quest):
        print(questions[quest])
for x in questions.keys():
    print(x, "\n", questions[x])
    import time
    time.sleep(10)
