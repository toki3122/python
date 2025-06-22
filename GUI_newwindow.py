from tkinter import *
def create_window():
    #new_window=Toplevel()#Toplevel() creates a new window over the existing window (dependent on the existing window) and Tk() creates an independent window
    new_window=Tk()
    window.destroy()#destroys the old window
window=Tk()
Button(window,text="create new window",command=create_window).pack()
window.mainloop()