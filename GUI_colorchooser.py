from tkinter import *
from tkinter import colorchooser
def click():
    window.config(bg=colorchooser.askcolor()[1])
window=Tk()
window.geometry("320x320")
button=Button(text="click here",command=click)
button.pack()
window.mainloop()