from tkinter import*
from tkinter import messagebox

win=Tk()
win.title("what next")
win.geometry("300x300+200+200")

sel=IntVar()
sel.set(1)

rbJob=Radiobutton(win,text="job",font=("courier",18,"bold italic"),Variable=sel,value=1)
rbMs=Radiobutton(win,text="Ms",font=("courier",18,"bold italic"),Variable=sel,value=2)
rbMba=Radiobutton(win,text="Mba",font=("courier",18,"bold italic"),Variable=sel,value=3)
rbMtech=Radiobutton(win,text="Mtech",font=("courier",18,"bold italic"),Variable=sel,value=4)

rbJob.grid("sticky=w")
rbMs.grid("sticky=w")
rbMba.grid("sticky=w")
rbMtech.grid("sticky=w")

def f1():
    res=sel.get()
    if res==1:
        msg="job"
    elif res==2:
        msg="Ms"
    elif res==3:
        msg="Mba"
    else:
        msg="Mtech"

    messagebox.showinfo("Selection",msg)

btnSubmit=Button(win,text="submit",font=("courier",18,"bold italic"),command=f1)
btnSubmit.grid()
win.mainloop()
