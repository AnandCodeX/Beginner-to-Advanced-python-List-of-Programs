#validation program control by try & except statment
class student:
    def __init__(self,r,n,m):
        self.rno=r
        self.name=n
        self.mark=m
    def show(self):
        print("rno=",self.rno)
        print("name=",self.name)
        print("marks=",self.mark)

try:
    rno=int(input("enter rno"))
    if rno<1:
        raise Exception("rno cannot be negative")
    name=input("enter name")
    if len(name)<2:
        raise Exception("name shoud be min 2 char")
    marks=int(input("enter marks"))
    if marks<0 or marks >100:
        raise Exception("marks shoud be under 100")
    s=student(rno,name,marks)
    s.show()

except Exception as e:
    print("bad input",e)