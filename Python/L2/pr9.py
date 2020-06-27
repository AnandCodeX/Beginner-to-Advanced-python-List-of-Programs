#wapp to read year and find if its a leap year


year=int(input("enter year "))

b1 = (year%100 != 0) and (year%4==0)                    #every 4 year
b2 = (year%100 == 0)  and (year%400==0)                 #every 400 year

if b1 or b2:
	print("yessss")
else:
	print("nooooo")