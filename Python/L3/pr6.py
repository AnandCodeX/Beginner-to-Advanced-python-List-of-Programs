#wapp to read marks from user find follow
#1)avg marks 2)higest marks 3)lowest marks 4)count nos >=70 5) count nos <=40

import array
marks=array.array("i",[])

num=int(input("enter no = "))

for i in range(num):
	m=int(input("enter marks = "))
	marks.append(m)
	
sum=0
for m in marks:
		sum = sum + m
avg = sum / num

print("average is =", avg)
		
high = low = marks[0]
if m > high:
	high=m
if m < low:
	low=m
print("highest marks =", high)
print("lowest marks =", low)

nos70,nos40=0,0

for m in marks:
    if m>=70:
        nos70=nos70+1
    if m<=40:
        nos40 = nos40+1
print(nos70)
print(nos40)        
    

				
		