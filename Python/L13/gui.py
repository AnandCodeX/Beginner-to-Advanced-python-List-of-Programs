from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import *

#Add window
def f1():
	root.withdraw()
	adst.deiconify()

#view window	
def f2():
	stViewData.delete(1.0,END)
	root.withdraw()
	vist.deiconify()
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select rno,name from student_thane_jan20"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
			msg=msg+"rno= "+str(d[0])+" name= "+str(d[1])+"\n"
			stViewData.insert(INSERT,msg)
	except DatabaseError as e:
		messagebox.showerror("Galat Kiya ",e)
	finally:
		if con is not None:			
			con.close()
			
#Add back button	
def f3():
	adst.withdraw()
	root.deiconify()

#View back button
def f4():
	vist.withdraw()
	root.deiconify()

#add submit button
def f5():
	con=None
	try:
		con=connect("system/abc123")
		rno=int(entAddRno.get())
		name=entAddName.get()
		args=(rno,name)
		
		cursor=con.cursor()
		sql="insert into student_thane_jan20 values('%d','%s')"
		cursor.execute(sql %args)
		con.commit()
		messagebox.showinfo("Sahi Kiya ",str(cursor.rowcount)+" rows inserted")
	except DatabaseError as e:
		messagebox.showerror("Galat Kiya ",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddRno.focus()
	
root=Tk()
root.title("S M S")
root.geometry("500x500+200+100")
root.configure(background='light blue')

btnAdd=Button(root,text="ADD",width=10,font=("arial",16,'bold'),command=f1)
btnAdd.pack(pady=20)

btnView=Button(root,text="VIEW",width=10,font=("arial",16,'bold'),command=f2)
btnView.pack(pady=20)



adst=Toplevel(root)
adst.title("Add Student")
adst.geometry("500x500+200+100")
adst.configure(background='light blue')
adst.withdraw()

lb1AddRno=Label(adst,text="Enter Roll.no ",font=("arial",16,'bold'))
lb1AddRno.pack(pady=10)

entAddRno=Entry(adst,bd=10,width=10,font=("arial",16,'bold'))
entAddRno.pack(pady=20)

lb1AddName=Label(adst,text="Enter Name ",font=("arial",16,'bold'))
lb1AddName.pack(pady=10)

entAddName=Entry(adst,bd=10,width=20,font=("arial",16,'bold'))
entAddName.pack(pady=20)

btnAddBack=Button(adst,text="BACK",width=10,font=("arial",16,'bold'),command=f3)
btnAddBack.pack(pady=20)

btnAddSave=Button(adst,text="SUBMIT",width=10,font=("arial",16,'bold'),command=f5)
btnAddSave.pack(pady=20)



vist=Toplevel(root)
vist.title("View Student")
vist.geometry("500x500+200+100")
vist.configure(background='light blue')
vist.withdraw()

stViewData=scrolledtext.ScrolledText(vist,width=40,height=10)
stViewData.pack(pady=10)

btnViewBack=Button(vist,text="Back",font=("arial",16,'bold'),command=f4)
btnViewBack.pack(pady=10)

root.mainloop()