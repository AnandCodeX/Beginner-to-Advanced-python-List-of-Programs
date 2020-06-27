#wapp to generate
#****
#***
#**
#*

num = int(input("entr number = "))

if num<0:
	print("be +ve")
else:
	for i in range(1,num-1):
		print(i*"*")
		num=num-1
		