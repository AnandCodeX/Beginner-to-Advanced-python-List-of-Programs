#wapp 
#i/p a,2,b,4,c,3
#o/p
#a a
#b b b 
#c c c

data="a,2,b,4,c,3"
list_of_data =data.split(",")

for i in range(0,len(list_of_data),2):
    w=list_of_data[i]
    h=int(list_of_data[i+1])
    print((w+"/t")*h)



