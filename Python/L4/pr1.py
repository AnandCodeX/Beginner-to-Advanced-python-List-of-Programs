#Wapp to read array of "n" integerss from user
#and count number of positive integers number of -ve
#integers and nunmbers of 0s

import array
data = array.array('i',[])

n=int(input("Enter number of element = "))
for i in range(n):
    ele=int(input("Enter element"))
    data.append(ele)

np,nn,nz = 0,0,0

for d in data:
    if (d>0):
        np=np+1
    elif (d<0):
        nn=nn+1
    else:
        nz=nz+1
print("Positive =", np,"negative =", nn, "Zero =", nz)                

