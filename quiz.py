name = ""
score = 0
questions = {"Q1:":
                 {"A:": "??",
                  "B:": "??",
                  "C:": "??"},
             "Q2:":
                 {"A:": "??"}}

for question in questions:
    print("\n",question)
    answers = questions[question]
    for answer in answers:
        print(answer,answers[answer])


#def ask(question_num):
