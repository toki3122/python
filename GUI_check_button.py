from tkinter import *
window=Tk()
def display():
    if x.get()==1:
        print("you are a human ^-^")
    else:
        print("of course you won't agree you robot!!")
x=IntVar()
photo=PhotoImage(file='F:\\tokee\\programming\\python\\code\\sans.png')
check_button=Checkbutton(window,text="I'm not a robot",variable=x,onvalue=1,offvalue=0,command=display,font=("arial",20),fg="#00ff00",bg="black",activebackground="black",activeforeground="#00ff00",padx=20,pady=20,image=photo,compound="left")
check_button.pack()
window.mainloop()