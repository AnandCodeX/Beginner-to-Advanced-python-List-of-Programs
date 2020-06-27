'''wapp to count the number of vowels and consonants'''

s1=input("enter string")
vc,cc = 0,0

for s in s1:
    if s.isalpha():
        if s in ['a','e','i','o','u','A','E','I','O','U']:
            vc=vc+1
        else:
            cc=cc+1
print("vowels=",vc,"consomamts=",cc)


