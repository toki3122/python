from tkinter import *
from tkinter import filedialog
def savefile():
    file=filedialog.asksaveasfile(defaultextension=".txt",filetypes=[
        ("text file",".txt"),
        ("html file",".html"),
        ("python file",".py"),
        ("all files",".*")
    ])
    if file is None:
        return
    filetext=str(text.get(1.0,END))
    file.write(filetext)
    file.close()
window=Tk()
button=Button(window,text="submit",command=savefile)
button.pack()
text=Text(window)
text.pack()
window.mainloop()