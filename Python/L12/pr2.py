from tkinter import*

root=Tk()
root.title("color me 2")
root.geometry("300x400+100+100")

def f(num):
    if num==1:
        root.configure(background="red")

    elif num==2:
        root.configure(background="green")

    else:
        root.configure(background="blue")


btnRed=Button(root,text='red',width=10,font=("arial",16,'bold'),command=lambda:f(1))
btnGreen=Button(root,text='green',width=10,font=("arial",16,'bold'),command=lambda:f(2))
btnBlue=Button(root,text='blue',width=10,font=("arial",16,'bold'),command=lambda:f(3))


btnRed.place(x=10,y=100)
btnGreen.place(x=100,y=50)
btnBlue.place(x=200,y=200)

root.mainloop()