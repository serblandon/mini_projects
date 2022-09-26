from tkinter import *
import PassGenModel

root = Tk()
root.title("PasswordGen")
root.config(bg='#F2B33D')
root.geometry("450x300")

def displayresult():
    aux = PassGenModel.genrndnb()
    label_result = Label(root, text=str(aux))
    label_result.place(x=180, y=180)
    print(aux)

label_intro = Label(root, background="orange", text="Welcome to the Password Generator"
                            "\nPress the button to generate a random number and see its length", font=("Helvetica", 10))

gen_button = Button(root, text="GENERATE", command=displayresult, background="light grey")

label_intro.place(x=30, y=10)

gen_button.place(x=190, y=150)


root.mainloop()