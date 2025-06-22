from tkinter import *
lan=["python","c++","c#"]
window=Tk()
def like():
    if x.get()==0:
        print("you like python?")
    elif x.get()==1:
        print("you like c++?")
    elif  x.get()==2:
        print("you like  c#?")
    else:
        print("eh?")
photo=PhotoImage(file='F:\\tokee\\programming\\python\\code\\python.png')
photo_1=PhotoImage(file='F:\\tokee\\programming\\python\\code\\c++.png')
photo_2=PhotoImage(file='F:\\tokee\\programming\\python\\code\\c#.png')
photos=[photo,photo_1,photo_2]
x=IntVar()
for i in range(len(lan)):
    radio=Radiobutton(window,text=lan[i],variable=x,value=i,padx=20,font=("impact",50),image=photos[i],compound="left",indicatoron=0,width=375,command=like)
    radio.pack()
window.mainloop()
