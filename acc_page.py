from tkinter import *
from subprocess import call
from tkinter import messagebox
root = Tk()

def nextp1():
    call(["python", "sign_up.py"])


def fakeclicks():
    messagebox.showinfo("no registered account"," please sign up")

lbl_1 = Label(root, text="WELCOME to GIN_BANK")
lbl_1.grid(row=0, column=0)

sign_in_button = Button(root, text="sign in", pady=20, padx=80, command=fakeclicks)
sign_in_button.grid(row=1, column=1)


sign_up_button = Button(root, text="sign up", pady=20, padx=80, command=nextp1)
sign_up_button.grid(row=1, column=2)


quit_button = Button(root, text="exit", padx=50, pady=10, command=quit)
quit_button.grid(row=2, column=3)
root.mainloop()