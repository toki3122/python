from tkinter import *
window=Tk()
def submit():
    food=[]
    for i in listbox.curselection():
        food.insert(i,listbox.get(i))
    print("you have ordered: ")
    for i in food:
        print(i)
def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())
def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())
listbox=Listbox(window,
                bg="#f7ffde",
                font=("cambria",20),
                width=12,
                selectmode=MULTIPLE)
listbox.pack()
listbox.insert(1,"falafel")
listbox.insert(2,"shwarma")
listbox.insert(3,"knafeh")
listbox.insert(4,"pasta")
listbox.insert(5,"applepie")
listbox.config(height=listbox.size())
entrybox=Entry(window)
entrybox.pack()
addbtn=Button(window,text="add",command=add)
addbtn.pack()
delbtn=Button(window,text="delete",command=delete)
delbtn.pack()
submitbtn=Button(window,text="submit",command=submit)
submitbtn.pack()
window.mainloop()