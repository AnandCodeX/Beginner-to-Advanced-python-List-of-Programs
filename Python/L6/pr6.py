#wapp to read list of marks & find the highest and lowest marks

marks=[]
reply=input("Do u wish to add intemarksger y/n")
while reply=='y':
    m=int(input("Enter marks"))
    marks.append(m)
    reply=input("Do u wish to add more marks y/n")

marks.sort()
lowest=marks[0]
highest=marks[-1]
print("lowest marks",lowest)
print("highest marks",highest)