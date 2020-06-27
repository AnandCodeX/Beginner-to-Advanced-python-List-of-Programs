#find area and circumference of circle for which RADIUS IS SUPPLIED by user
#hint : use math whenevre possible

import math
radius=float(input("enter radius"))
area=math.pi*math.pow(radius,2)
circumference=2*math.pi*radius

print("area = ",round(area,2))
print("circumferenmce = ",round(circumference,2))