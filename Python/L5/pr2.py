#wapp to read  2 strings from the user and check if theyare anagrams.
# s1=listen s2=silentr

def mysort(s):
    d=sorted(s)
    r=''.join(d)
    return r
s1=input("Enter 1 String")
s2=input("Enter 2 String")

ns1=mysort(s1)
ns2=mysort(s2)

if ns1==ns2:
    print("anagram")
else:
    print("not anmagram")