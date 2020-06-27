#wapp to find factorial of a number non recursive

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

num=int(input("Enter no"))

if num<0:
    print("b+ve")
else:
    res=fact(num)
    print("Factorial is =",fact)