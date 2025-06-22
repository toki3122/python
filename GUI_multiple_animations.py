from tkinter import *
import time
class ball:
    def __init__(self,canvas,x,y,d,Vx,Vy,color):
        self.canvas=canvas
        self.image=canvas.create_oval(x,y,d,d,fill=color)
        self.Vx=Vx
        self.Vy=Vy
    def move(self):
        coordinates=self.canvas.coords(self.image)
        print(coordinates)
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.Vx=-self.Vx
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.Vy=-self.Vy
        self.canvas.move(self.image,self.Vx,self.Vy)
window=Tk()
WIDTH=500
HEIGHT=500
canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
volleyball=ball(canvas,0,0,100,2,2,"white")
tennisball=ball(canvas,0,0,50,4,3,"yellow")
basketball=ball(canvas,0,0,90,3,4,"#e25300")
ttball=ball(canvas,0,0,20,4,5,"#fc8b4a")
while True:
    volleyball.move()
    tennisball.move()
    basketball.move()
    ttball.move()
    window.update()
    time.sleep(0.01)
window.mainloop()