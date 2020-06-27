from tkinter import*

root=Tk()
root.title("color me")
root.geometry("300x400+300+200")

def f1():
    root.configure(background="red")

def f2():
    root.configure(background="blue")

def f3():
    root.configure(background="green")

btnRed=Button(root,text='red',width=10,font=("arial",16,'bold'),command=f1)
btnBlue=Button(root,text='Blue',width=10,font=("arial",16,'bold'),command=f2)
btnGreen=Button(root,text='Green',width=10,font=("arial",16,'bold'),command=f3)

btnRed.pack(pady=20)
btnGreen.pack(pady=20)
btnBlue.pack(pady=20)

root.mainloop()