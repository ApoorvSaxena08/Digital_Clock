from tkinter import Tk
from tkinter import Label
import time
import sys

root = Tk()
root.title("Digital Clock")

def curr_time():
    display = time.strftime("%I:%M:%S %p")
    digi.config(text = display)
    digi.after(200,curr_time)

digi = Label(root,font=("arial",150),bg="black",fg="white")
digi.pack()

curr_time()
root.mainloop()
