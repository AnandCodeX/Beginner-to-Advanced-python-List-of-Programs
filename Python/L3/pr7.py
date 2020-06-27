#wapp to find factorial of a number

def fact(n):
    f=1

    for i in range(1,n+1):
        f=f*1
            return f

num=int(input("Enter no"))

if num<0:
    print("b+ve")
elif num == 0 or num==1:
    print("fact=",1)
else:
    res=fact(num)
    print("Factorial is =",fact)