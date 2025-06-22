from tkinter import *
def d_start(event):
    widget=event.widget# so that we can use any widget
    widget.startX=event.x
    widget.startY=event.y
def d_motion(event):
    widget=event.widget
    x=widget.winfo_x()-widget.startX+event.x #new_coordinate=zeroth coordinate w.r.t. the window-cursor movement start pos+cursor movement
    y=widget.winfo_y()-widget.startY+event.y
    widget.place(x=x,y=y)
window=Tk()
label1=Label(window,bg="red",width=10,height=5)
label1.place(x=0,y=0)
label2=Label(window,bg="blue",width=10,height=5)
label2.place(x=50,y=50)
label1.bind("<Button-1>",d_start)
label1.bind("<B1-Motion>",d_motion)
label2.bind("<Button-1>",d_start)
label2.bind("<B1-Motion>",d_motion)
window.mainloop()