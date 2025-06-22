from tkinter import *

window=Tk()
firstnamelabel=Label(window,text="First name: ",width=20,bg="#00ff00").grid(row=0,column=0)
firstnameentry=Entry(window).grid(row=0,column=1)
lastnamelabel=Label(window,text="Last name: ",bg="red").grid(row=1,column=0)
lastnameentry=Entry(window).grid(row=1,column=1)
emaillabel=Label(window,text="Email: ",bg="blue",width=30).grid(row=2,column=0)
emailentry=Entry(window).grid(row=2,column=1)
Button(window,text="Submit").grid(row=3,column=0,columnspan=2)
window.mainloop()