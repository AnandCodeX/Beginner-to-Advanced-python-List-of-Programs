#wapp to find factorial mo

num=int(input("Entwer the no = "))
if num < 0 :
	print("Be +ve")
elif num == 0 or num == 1:
	print("ans = ", 1)
else:
	fact = 1
	for i in range(1,num+1):
		fact = fact * i
	else:
		print("ans = ", fact)