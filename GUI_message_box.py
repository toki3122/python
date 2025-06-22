from tkinter import *
from tkinter import messagebox
def click():
    #messagebox.showinfo(title="info",message="hello there")

    #messagebox.showwarning(title="WARNING!",message="YOU HAVE A VIRUS!!!!")

    #messagebox.showerror(title="ERROR!",message="YOU HAVE A VIRUS!!!!")

    # if messagebox.askokcancel(title="ask",message="erase #$%#@%$^^%&?"):
    #     print("good")
    # else:
        # print("you should have erased it")

    #  if messagebox.askretrycancel(title="ask",message="erase #$%#@%$^^%&?"):
    #     print("good")
    #  else:
    #     print("you should have erased it")

    # if messagebox.askyesno(title="ask",message="like cake?"):
    #     print("same")
    # else:
    #     print("why not?")
    # answer=messagebox.askquestion(title="ask",message="pie eater?")
    # if answer=="yes":
    #     print("you weirdo!")
    # else:
    #     print("same")
    answer=messagebox.askyesnocancel(title="ask",message="do you like coding?")
    if answer==True:
        print("good for you!! ^-^")
    elif answer==False:
        print("why?? :(")
    else:
        print("what? =_=")
window=Tk()
button=Button(window,text="click me!",command=click)
button.pack()
window.mainloop()