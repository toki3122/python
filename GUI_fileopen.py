from tkinter import *
from tkinter import filedialog
def fileopen():
    file=open(filedialog.askopenfilename(initialdir="F:\\tokee\\programming\\C++\\competitive programming",filetypes=(("text files","*.txt"),("all files","*.*"))),'r')
    print(file.read())
#not really necessary to add initialdir
window=Tk()
button=Button(window,text="submit",command=fileopen)
button.pack()
window.mainloop()
