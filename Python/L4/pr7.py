#wapp read string to find its palindrome

s1=input("Enter a sttring = ")
# '''s1 = s1.lower()'''  #if u want case insensative

r1=s1[::-1]

if s1==r1:
    print("yesssss")
else:
    print("noooooo")
