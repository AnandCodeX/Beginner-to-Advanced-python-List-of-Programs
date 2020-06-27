#wapp to read marks and display grades

marks=int(input("enter marks "))



if marks>=70:
	print("distinct")
elif marks>=60:
	print("first")
elif marks>=50:
	print("Secound")
elif marks>=40:
	print("pass")
else:
	print("fail")