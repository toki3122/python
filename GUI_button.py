from tkinter import *
count=0
def click():
    global count
    count+=1
    print(count)
window=Tk()
photo=PhotoImage(file='F:\\tokee\\programming\\python\\code\\sans.png')
button=Button(window,text="click me!",command=click,font=('jokerman',30),fg="#00ff00",bg="black",activeforeground="#00FF00",activebackground="black", image=photo,compound="top")
button.pack()
window.mainloop()