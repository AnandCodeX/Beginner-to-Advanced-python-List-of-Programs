#wapp to o/p yes if user enter int else no

try:
    num=int(input("enter integer"))
    print("yes")

except ValueError:
    print("no")