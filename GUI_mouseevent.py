from tkinter import *
def fun(event):
    print("mouse coordinates: "+str(event.x)+","+str(event.y))
window=Tk()
#general structure: window.bind(event,function)
#window.bind("<Button-1>",fun) #LMB
#window.bind("<Button-2>",fun) #scroll wheel
#window.bind("<Button-3>",fun) #RMB
#window.bind("<ButtonRelease>",fun)
#window.bind("<Enter>",fun)
#window.bind("<Leave>",fun)
window.bind("<Motion>",fun)
window.mainloop()