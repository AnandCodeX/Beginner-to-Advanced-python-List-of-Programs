#wa object oriented python program for class rectangle:
# length and width
#show()
#area()
#perimeter()

class rectangle:
    def __init__(self,le,wi):
        self.length=le
        self.width=wi

    def show(self):
        print("length =",self.length)
        print("width = ",self.width)
    def area(self):
        ans=self.length*self.width
        print("area = ",ans)

    def perimeter(self):
        ans=2*(self.length + self.width)
        print("perimeter = ",ans)

length=float(input("enter length"))
width=float(input("enter width"))
r=rectangle(length,width)
r.show()
r.area()
r.perimeter()
