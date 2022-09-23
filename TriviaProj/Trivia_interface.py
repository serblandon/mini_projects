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

root.title("CapitalsGame")

mylabel1 = Label(root,
                 text="Instructions: In order to get your answer validated you need to press the 'Check' button first and then 'Next"
                      ""
                      "Welcome! "
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


def check_button():
    global result
    global i
    global e
    if e.get() == listt[options[i]]["answer"]:
        result += 1
        label_state = Label(root, text="Correct", fg="Green")
        label_state.pack()
    else:
        label_state = Label(root, text="Incorrect", fg="Red")
        label_state.pack()


i = -1


def button_yes_act():
    global result
    global i
    global e

    i += 1

    label_question = Label(root, text=listt[options[i]]["question"])
    label_question.pack()
    label_possanswers = Label(root, text=listt[options[i]]["possanswers"])
    label_possanswers.pack()
    label_ques = Label(root, text="Your answer is:")
    label_ques.pack()
    e = Entry(root)
    e.pack()
    button_check = Button(root, text="Check", command=check_button)
    button_check.pack()
    if i < len(options) - 1:
        button_submit = Button(root, text="Next", command=button_yes_act)
        button_submit.pack()
    else:
        button_submittt = Button(root, text="Submit", command=button_submitt)
        button_submittt.pack()


options = random.sample(range(0, len(listt)), 3)
print(options)

label_text1 = Label(root, text="Let's begin...\n", font=6)
label_text1.pack()

button_yes = Button(root, text="Yes", font=50, command=button_yes_act)
button_yes.pack()

button_no = Button(root, text="No", font=1, command=button_no_act)
button_no.pack()

root.mainloop()
