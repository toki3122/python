from tkinter import *
from tkinter import ttk
window=Tk()
notebook=ttk.Notebook(window)#for tabs management
tab1=Frame(notebook)
tab2=Frame(notebook)
notebook.add(tab1,text="tab 1")
notebook.add(tab2,text="tab 2")
notebook.pack(expand=True,fill="both")
Label(tab1,text="hello this is tab1 ",width=50,height=25).pack()
Label(tab2,text="bye this is tab2 ",width=50,height=25).pack()
window.mainloop()