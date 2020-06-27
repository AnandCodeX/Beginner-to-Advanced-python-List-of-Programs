s1=input("enter string")
count_letter = {}
for s in s1:
    ans=count_letter.get(s,-1)
    if ans==-1:
        count_letter[s]=1
    else:
        count_letter[s]=ans+1

print(count_letter)
