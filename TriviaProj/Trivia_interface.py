from tkinter import *
import random

listt = [
    {
        "question": "What is the capital of France?",
        "answer": "a",
        "possanswers": "a)Paris "
                       "b)Seville "
                       "c)Marseille "
    },
    {
        "question": "What is the capital of Spain?",
        "answer": "c",
        "possanswers": "a)Barcelona "
                       "b)Malaga "
                       "c)Madrid "
    },
    {
        "question": "What is the capital of Japan?",
        "answer": "a",
        "possanswers": "a)Tokyo "
                       "b)Osaka "
                       "c)Shanghai "
    },
    {
        "question": "What is the capital of Mexico?",
        "answer": "a",
        "possanswers": "a)Mexico City "
                       "b)Guadalajara "
                       "c)Kingston "
    },
    {
        "question": "What is the capital of Egypt?",
        "answer": "b",
        "possanswers": "a)Casablanca "
                       "b)Cairo "
                       "c)Lagos "
    },
    {
        "question": "What is the capital of Canada?",
        "answer": "c",
        "possanswers": "a)Toronto "
                       "b)Montreal "
                       "c)Ottawa "
    },
    {
        "question": "What is the capital of Australia?",
        "answer": "a",
        "possanswers": "a)Canberra "
                       "b)Sydney "
                       "c)Brisbane "
    }
]
result = 0

root = Tk()

mylabel1 = Label(root, text="Welcome! "
                            "Do you want to play?", font=10)
mylabel1.pack()


def button_submitt():
    global result
    label_score = Label(root, text=str(result))
    label_score.pack()


def button_no_act():
    quit(1)


def button_correct():
    global result
    result += 1


'''def button_yes_act():
    global result

    label_text1 = Label(root, text="Let's begin...\n", font=6)
    label_text1.pack()
    options = random.sample(range(len(listt)), 3)
    for i in options:
        label_question = Label(root, text=listt[i]["question"])
        label_question.pack()
        label_possanswers = Label(root, text=listt[i]["possanswers"])
        label_possanswers.pack()
        label_ques = Label(root, text="Your answer is:")
        label_ques.pack()
        e1 = Entry(root)
        e1.pack()
        if e1.get() == listt[i]["answer"]:
            result += 1

    button_submit = Button(root, text="Submit", command=button_submitt)
    button_submit.pack()'''

def button_yes_act(i):
    global result

    label_question = Label(root, text=listt[i]["question"])
    label_question.pack()
    label_possanswers = Label(root, text=listt[i]["possanswers"])
    label_possanswers.pack()
    label_ques = Label(root, text="Your answer is:")
    label_ques.pack()
    e1 = Entry(root)
    e1.pack()
    if e1.get() == listt[i]["answer"]:
        result += 1


def function():
    options = random.sample(range(len(listt)), 3)
    for i in options:
        button_yes_act(i)
    button_submit = Button(root, text="Submit", command=button_submitt)
    button_submit.pack()


button_yes = Button(root, text="Yes", font=50, command=function)
button_yes.pack()

button_no = Button(root, text="No", font=1, command=button_no_act)
button_no.pack()


label_text1 = Label(root, text="Let's begin...\n", font=6)
label_text1.pack()





root.mainloop()
