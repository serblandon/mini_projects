from tkinter import *
import PassGenModel
from tkinter import messagebox


root = Tk()
root.title("PasswordGen")
# root.config(bg='#F2B33D')
root.geometry("500x300")


def gen_password():
    psw_box.delete(0, END)
    psw_length_entry.delete(0, END)
    password = ""
    length = ""
    password, length = PassGenModel.genrndnb()

    psw_box.insert(0, password)
    psw_length_entry.insert(0, length)


def cpy_clip():
    root.clipboard_clear()
    root.clipboard_append(psw_box.get())
    #calling popup method to display the copied info
    popup()


def popup():
    messagebox.showinfo("Popup", "Copied to clipboard")


#intro message
label_intro = Label(root, text="Welcome to the Password Generator"
                                    "\nPress the button to generate a random number and see its length",
                         font=("Helvetica", 10))
label_intro.pack()

#LabelFrame for password length
psw_length = LabelFrame(root, text="Password Length:")
psw_length.pack(pady=20)

#LabelFrame for password
psw = LabelFrame(root, text="Password:")
psw.pack(pady=20)

#Entry box for password
psw_box = Entry(psw, text="", font=("Helvetica", 10), border=0, bg="systembuttonface")
psw_box.pack()

#Entry box for length
psw_length_entry = Entry(psw_length, font=("Helvetica", 10), border=0, bg="systembuttonface")
psw_length_entry.pack()

#Button Frame
frame1 = Frame(root)
frame1.pack()

#Buttons for generation and for copying
button_gen = Button(frame1, text="Generate Password", command=gen_password)
button_gen.grid(row=0, column=0, padx=10)

button_cpy = Button(frame1, text="Copy to Clipboard", command=cpy_clip)
button_cpy.grid(row=0, column=2, padx=10)


#end
root.mainloop()