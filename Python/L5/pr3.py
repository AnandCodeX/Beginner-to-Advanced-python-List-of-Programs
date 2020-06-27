#wapp read sentence and sort every word in sentence

sentence=input("Enter sentence")
data=sentence.split(" ")

def mysort(s):
    d=sorted(s)
    r=''.join(d)
    return r

new_sentence = ""
for d in data:
        new_sentence = new_sentence + " "+mysort(d)
print("original = ",sentence)
print("new = ",new_sentence)
