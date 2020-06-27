#wapp 

def area(p1=None,p2=None):
    if p1 is not None and p2 is None:
        ans=3.14*radius*radius
        return ans
    elif p1 is not None and p2 is not None:
        ans=p1*p2
        return ans


while True:
    op=int(input("1 area of cirlcle, 2 area of rectangle, 3 exit"))
    if op==1:
        radius = float(input("enter radius"))
        ans=area(radius)
        print("area = ",ans)
    elif op==2:
        length = float(input("Enter length"))
        width = float(input("Enter width"))
        ans=area(length,width)
        print("area = ", ans)
    elif op==3:
        break
    else:
        print("invalid option")
