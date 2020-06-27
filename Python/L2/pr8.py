#wapp to read  3 int no find  max



n1=int(input("enter a number 1 ="))
n2=int(input("enter a number 2 ="))
n3=int(input("enter a number 3 ="))
if n1>n2:
	max = n1
else:
	max = n2
if n3>max:
	max=n3

print("max = ",max)