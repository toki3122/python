from tkinter import *
window=Tk()
canvas=Canvas(window,width=500,height=500)
canvas.create_line(0,0,500,500,fill="blue",width=5)
canvas.create_polygon(250,0,500,500,0,500,fill="yellow",outline="black",width=5)
canvas.create_arc(0,0,500,500,fill="#4d960a",start=90)
canvas.create_arc(0,0,500,500,fill="#d80505",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="#eeeeee",start=180,extent=180,width=10)
canvas.create_oval(190,190,310,310,fill="white",width=10)
canvas.pack()
window.mainloop()