from tkinter import *
def move_up(event):
    canvas.move(myimage,0,-5)
def move_down(event):
    canvas.move(myimage,0,5)
def move_left(event):
    canvas.move(myimage,-5,0)
def move_right(event):
    canvas.move(myimage,5,0)
window=Tk()
window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)
canvas=Canvas(window,width=600,height=600)
canvas.pack()
photoimage=PhotoImage(file='F:\\tokee\\programming\\python\\code\\assets\\Jump.png')
myimage=canvas.create_image(0,0,image=photoimage,anchor=NW)
window.mainloop()