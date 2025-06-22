from tkinter import *
def submit():
    print(textarea.get("1.0",END))
window=Tk()
textarea=Text(window,
              bg="light yellow",
              font=("ink free",25),
              width=20,
              height=8,
              padx=20,
              pady=20)
textarea.pack()
button=Button(window,text="submit",command=submit)
button.pack()
window.mainloop()