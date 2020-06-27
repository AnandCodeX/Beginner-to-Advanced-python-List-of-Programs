#waoopp class circle
#radius
#display()
#area()
#circumference()

class circle:
    def __init__(self,r):
        self.radius=r
    def show(self):
        print("radius = ",self.radius)
    def area(self):
        ans=3.14159*self.radius**2
        print("radius = ",round(ans,2))
    def circumference(self):
        ans=2*3.14159*self.radius
        print("circumference = ",round(ans,2))

r=float(input("enter radius"))
c=circle(r)
c.show()
c.area()
c.circumference()
        