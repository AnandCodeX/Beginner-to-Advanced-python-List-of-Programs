#wapp to read sentence and reverse the sentence with every word too reverse

sentence=input("Enter sentence")
data=sentence.split(" ")

for d in data:
    #reverse every word and reverse the sentence
    new_sentence = sentence[::-1]
    #Other way #new_sentence=d[::-1]+""+new_sentence
print("original",sentence)
print("new",new_sentence)