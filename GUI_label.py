from tkinter import *
#an area that holds text and/or an image within a window
window=Tk()
photo=PhotoImage(file='F:\\tokee\\programming\\python\\code\\sans.png')
label=Label(window,text="hello world",font=('Arial',40,'bold'),fg="#ffffff",bg='#1a7692',relief=RAISED,bd=10,padx=20,pady=20,image=photo,compound='top')
label.pack()
#label.place(x=0,y=0)
window.mainloop()