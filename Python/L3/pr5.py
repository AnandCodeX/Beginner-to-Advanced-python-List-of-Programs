#aaaa
#bbb
#cc
#a


num=int(input("enter no"))
if num<0:
    print("be +ve")
else:
    ch=97
    for i in range(num,0,-1):
        print(i*(chr(ch)+ "\t"))
        ch=ch+1
        