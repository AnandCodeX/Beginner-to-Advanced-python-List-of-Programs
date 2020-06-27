#wapp to read tuple of integers from the user and display in decending order

list_data=[]
tup_data=()

reply=input("Do u wish to add int y/n")
while reply=='y':
    ele=input("Enter name")
    list_data.append(ele)
    reply=input("Do u wish to add more int y/n")

tup_data=tuple(list_data)
print("befor = ",tup_data)

list_data.sort(reverse=True)
tup_data=tuple(list_data)
print("after = ",tup_data)