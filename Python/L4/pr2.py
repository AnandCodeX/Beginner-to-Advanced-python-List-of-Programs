#Wapp menu driven 


import array
data = array.array('i',[])

n=int(input("Enter number of element = "))
for i in range(n):
    ele=int(input("Enter element"))
    data.append(ele)

while True: # by the true it will be infinite
    op=int(input("1 data, 2 data in asc, 3 data in dec, 4 exit"))
    if op==1:
        for d in data:
            print(d, end='')
        print()

    elif op==2:
        adata=sorted(data)
        for d in adata:
            print(d,end=" ")

    elif op==3:
        ddata=sorted(data, reverse=True)
        for d in ddata:
            print(d,end=" ")


    elif op==4:
        break
    else:
        print("invalid option")