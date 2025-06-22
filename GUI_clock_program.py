from tkinter import *
from time import *
def update():
    time_string=strftime("%I:%M:%S %p")
    label.config(text=time_string)
    day_string=strftime("%A")
    label1.config(text=day_string)
    date_string=strftime("%B %d, %Y")
    label2.config(text=date_string)
    window.after(1000,update)
window=Tk()
label=Label(window,font=("arial",50),bg="#000000",fg="#ff0000")
label.pack()
label1=Label(window,font=("ink free",15))
label1.pack()
label2=Label(window,font=("ink free",20))
label2.pack()
update()
window.mainloop()