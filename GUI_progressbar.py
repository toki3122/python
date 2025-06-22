from tkinter import *
from tkinter.ttk import *
import time
import random
def start():
    GB=100
    Download=0
    speed=1
    while(Download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        Download+=speed
        percent.set(str(int((Download/GB)*100))+"%")#setting the value with a specific algorithm
        text.set(str(Download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()
window=Tk()
percent=StringVar()
text=StringVar()
bar=Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)
percentlabel=Label(window,textvariable=percent).pack()#textvariable=prints the value of a specific variable(can be changed)
tasklabel=Label(window,textvariable=text).pack()
Button(window,text="download",command=start).pack()
window.mainloop()