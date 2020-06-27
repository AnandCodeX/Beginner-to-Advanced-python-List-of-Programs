#wapp to find the sum of n integers
# 1+2+3+4+5=15

num=int(input("enter number"))


if num< 0:
	print("be +ve")
else:
	sum = 0
	i = 1
	while i <= num:
		sum = sum+i
		i = i + 1
	print("sum = ",sum)