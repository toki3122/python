from tkinter import *
window=Tk()
def msg():
    print("the temp is: ",scale.get()," degrees celsius")
hotphoto=PhotoImage(file='F:\\tokee\\programming\\python\\code\\fire.png')
hotlabel=Label(image=hotphoto)
hotlabel.pack()
scale=Scale(window,from_=100,to=0,length=300,orient=VERTICAL,font=("consolas",20),tickinterval=10,resolution=5,fg="red",bg="black",troughcolor="#69eaff",)
scale.set(((scale["from"]-scale["to"])/2)+scale["to"])
scale.pack()
coldphoto=PhotoImage(file='F:\\tokee\\programming\\python\\code\\flake.png')
coldlabel=Label(image=coldphoto)
coldlabel.pack()
button=Button(window,text="submit",command=msg)
button.pack()
window.mainloop()