#wapp to read list of integers from user and print onm the screen

num=[]
reply=input("Do u wish to add integer y/n")
while reply=='y':
    ele=int(input("Enter integer"))
    num.append(ele)
    reply=input("Do u wish to add more integer y/n")

print(num)

for n in num:
    print(n,end='')
print()

for i in range(len(num)):
    print(num[i],end='')