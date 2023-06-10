from tkinter import *
from subprocess import call
import os
from PIL import Image

root= Tk()
###################################################
###################################################
def nextp1():
    call(["python", "acc_page.py"])

root.title("GIN-Bank")

button1 = Button(root, text="welcome", padx=200, pady=20, command=nextp1)
button1.grid(row=0, column=0)

button_quit = Button(root, text="exit program", command=root.quit)
button_quit.grid(row=1, column=2)

root.mainloop()