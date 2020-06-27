#WAPP TO READ 2 set of student name 
# 1- android batch student
# 2- java batch student
# o/p 1- all name 
# 2-common name

android =set()
java=set()

reply=input("Do u wish to add android student name y/n")
while reply=='y':
    n=input("Enter name")
    android.add(n)
    reply=input("Do u wish to add more java student name y/n")

reply=input("Do u wish to add java student name y/n")
while reply=='y':
    n=input("Enter name")
    java.add(n)
    reply=input("Do u wish to add more java student name y/n")

r1 = android | java;  print("All student",r1)
r2 = android & java;  print("common student",r2)