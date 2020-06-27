from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('even odd calsi')

root.geometry('500x400+200+100')

def f1():
    try:
        s = entNumber.get()
        num = int(s)
        msg =''
        if num % 2 == 0:
            msg = 'even'
        else:
            msg = 'odd'
        messagebox.showinfo('jawab',msg)
    except ValueError:
        messagebox.showerror('galat kiya','int only')
        entNumber.delete(0,END)
        entNumber.focus()

lblNumber = Label(root,text='enter number',font = ('Courier',30,'bold italic'))
lblNumber.pack(pady = 10)

entNumber = Entry(root,bd=10,font = ('Courier',30,'bold italic'))
entNumber.pack(pady = 20)

btnFind = Button(root,text='find',font = ('Courier',30,'bold italic'),command = f1)
btnFind.pack()



root.mainloop()