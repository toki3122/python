from tkinter import *
import time
WIDTH=600
HEIGHT=600
Vx=3.5
Vy=2
window=Tk()
canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
background=PhotoImage(file='F:\\tokee\\programming\\python\\code\\space.png')
myinage=canvas.create_image(0,0,image=background)
photoimage=PhotoImage(file='F:\\tokee\\programming\\python\\code\\alien.png')
myimage=canvas.create_image(0,0,image=photoimage,anchor=NW)
photo_width=photoimage.width()
photo_height=photoimage.height()
while True:
    coordinates=canvas.coords(myimage)
    print(coordinates)
    if(coordinates[0]>=WIDTH-photo_width or coordinates[0]<0):
        Vx=-Vx
    if(coordinates[0]>=HEIGHT-photo_height or coordinates[0]<0):
        Vy=-Vy
    canvas.move(myimage,Vx,Vy)
    window.update()
    time.sleep(0.01)
window.mainloop()