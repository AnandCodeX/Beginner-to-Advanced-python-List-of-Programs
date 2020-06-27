"""pickle"""

import os.path
import pickle

class student:
	def __init__(self,rno,name):
		self.rno=rno
		self.name=name
		
	def show(self):
		print("rno = ",self.rno)
		print("name = ",self.name)
		
list_of_students =[]
file_name ="student ka data.ser"

if os.path.isfile(file_name):
	with open(file_name,"rb") as f:
		list_of_students=pickle.load(f)

while True:
	op=int(input("1.add  2.view  3.delete  and 4.exit "))
	if op==1:
		rno=int(input("enter rno "))
		name = input("enter name ")
		s=student(rno,name)
		list_of_students.append(s)
		print("record saved ")
		
	elif op==2:
		for d in list_of_students:
			d.show()
			
	elif op==3:
		rno=int(input("enter the rno to be deleted "))
		for e in list_of_students:
			if e.rno== rno:
				list_of_students.remove(e)
		print(rno," deleted")
	elif op==4:
		with open(file_name,"wb") as f:
			pickle.dump(list_of_students,f)
		break
		
	else:
		print("invalid option ")