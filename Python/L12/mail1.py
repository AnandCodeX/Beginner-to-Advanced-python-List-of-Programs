#for sending information via mail
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Kamal Classes App")
root.geometry("300x500+300+100")

lblName=Label(root,text="Name",font=("arial",18,"bold"))
entName=Entry(root,bd=10,font=("arial",18,"bold"))
lblName.grid()
entName.grid()

lblFeedback=Label(root,text="Feedback",font=("arial",18,"bold"))
f=IntVar()
f.set(1)

rbF=Radiobutton(root,text="Fantastic",font=("arial",18,"bold"),variable=f,value=1)
rbS=Radiobutton(root,text="Superb",font=("arial",18,"bold"),variable=f,value=2)
rbE=Radiobutton(root,text="Excellent",font=("arial",18,"bold"),variable=f,value=3)
lblFeedback.grid()
rbF.grid(sticky="w")
rbS.grid(sticky="w")
rbE.grid(sticky="w")

lblMaterials=Label(root,text="Materials",font=("arial",18,"bold"))

s,n,c=IntVar(),IntVar(),IntVar()
cbSoftware=Checkbutton(root,text="Software",font=("arial",18,"bold"),variable=s)
cbNotes=Checkbutton(root,text="Notes",font=("arial",18,"bold"),variable=n)
cbCertificate=Checkbutton(root,text="Certificate",font=("arial",18,"bold"),variable=c)
lblMaterials.grid(sticky="w")
cbSoftware.grid(sticky="w")
cbNotes.grid(sticky="w")
cbCertificate.grid(sticky="w")

def f1():
    name=entName.get()
    if len(name) < 2 or not name.isalpha():
        messagebox.showerror("Wrong","Invalid Name")
        entName.delete(0,END)
        entName.focus()
        return
    
    fe = f.get()
    if fe==1:
        feedback="fantastic"
    elif fe==2:
        feedback="superb"
    else:
        feedback="Excellent"
    
    materials=""
    if s.get()==1:
        materials=materials+"Software"
    if n.get()==1:
        materials=materials+"Notes"
    if c.get()==1:
        materials=materials+"Certificate"
    msg="Name = "+ name + "\nFeedback = "+ feedback +"\nMaterials = "+ materials
    messagebox.showinfo("Msg",msg)

    to ="kanalsir@ymail.com"
    subject="feedback"+ name
    text=msg
    import smtplib
    sender="anandrtiwarilt26i@gmail.com"
    password="0911850047"
    message='Subject:{}\n\n{}'.format(subject,Text)
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(sender,password)
    print("logged in")

    try:
        server.sendmail(sender,to,message)
        print("email sent")
    except:
        print("error sending mail")
    server.quit
btnSubmit=Button(root,text="Submit",font=("arial",18,"bold"),command=f1)
btnSubmit.grid()
root.mainloop()