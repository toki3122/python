from tkinter import *
#widgets=GUI elements: buttons, textboxes, labels, images
#windows=serves as container to hold or contain these widgets
window=Tk()#instantiate an instance of a window
window.geometry("640x640")
window.title("tokiGUI")
icon=PhotoImage(file='F:\\tokee\\programming\\python\\code\\sans.png')
window.iconphoto(True,icon)
window.config(background="#2883A7")
window.mainloop()#place window on screen, listen for events