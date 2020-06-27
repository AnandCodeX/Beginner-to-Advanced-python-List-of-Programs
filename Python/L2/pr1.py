#wapp to read radius of circle and find area and 
#circumference of circle

radius=float(input("enter the radius "))
area = 3.14159 * radius ** 2
circumference = 2 * 3.14159 * radius
print("area is =",round(area,3))
print("circumference is =", round(circumference,3))

#complex way
 
print("area is =%.3f" %area)