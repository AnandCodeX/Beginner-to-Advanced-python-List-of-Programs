#wapf that takes as input int returns true is 
# # the no is arsmstrong no else return false

def check(num):
    org_num = num
    sum = 0
    while num>0:
        digit =num%10
        sum =sum+digit**3
        num =num//10
    if(org_num==sum):
        return True
    else:
        return False

n=int(input("Enter the number ="))
if n<0:
    print("be +ve")
else:
    if check (n):
        print("yes")
    else:
        print("no")