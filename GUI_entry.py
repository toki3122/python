#textbox that accepts a single line of user input
from tkinter import *
window=Tk()
def submit():
    username=entry.get()
    print("hello "+username)
    entry.config(state=DISABLED)
def delete():
    entry.delete(0,END)
def back_space():
    entry.delete(len(entry.get())-1,END)
entry=Entry(font=("arial",50),fg="#00ff00",bg="black",show="*")
entry.pack(side=LEFT)
#entry.insert(0,'spongebob') #default entry
button=Button(window,text="submit",command=submit)
button.pack(side=RIGHT)
button_1=Button(window,text="delete",command=delete)
button_1.pack(side=RIGHT)
button_2=Button(window,text="<x",command=back_space)
button_2.pack(side=RIGHT)
window.mainloop()