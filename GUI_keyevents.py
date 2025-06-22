from tkinter import *
def fun(event):
    #print("you pressed: "+event.keysym)
    label.config(text=event.keysym)
window=Tk()
window.bind("<Key>",fun)
label=Label(window,font=("helvetica",100))
label.pack()
window.mainloop()