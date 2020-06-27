#wapp to read  2 strings from the user and check if theyare anagrams.
# s1=listen s2=silentr

s1=input("Enter 1 String")
s2=input("Enter 2 String")

sn1=sorted(s1)
ns1=''.join(sn1)
sn2=sorted(s2)
ns2=''.join(sn2)

if sn1==sn2:
    print("anagram")
else:
    print("not anmagram")