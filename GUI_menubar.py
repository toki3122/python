from tkinter import *
from tkinter import filedialog
window=Tk()
def fileopen():
    file=open(filedialog.askopenfilename(filetypes=(("text file","*.txt"),("all files","*.*"))),'r')
    print(file.read())
def savefile():
    print("file saved")
def cut():
    print("cut file chop chop")
def copy():
    print("copy file blem blem")
def paste():
    print("paste file stick stick")
# openimage=PhotoImage(file="open.png")
# saveimage=PhotoImage(file="save.png")
# quitimage=PhotoImage(file="quit.png")
menubar=Menu(window)
window.config(menu=menubar)
filemenu=Menu(menubar,tearoff=0)#so there will be a dropdown menu in a menubar
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="open",command=fileopen) #adding options to the dropdown menubar
filemenu.add_command(label="save",command=savefile)
filemenu.add_separator()
filemenu.add_command(label="exit",command=quit)
editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="edit",menu=editmenu)
editmenu.add_command(label="cut",command=cut)
editmenu.add_command(label="copy",command=copy)
editmenu.add_command(label="paste",command=paste)
window.mainloop()