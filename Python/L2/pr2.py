#wapp convert F to C 


fah= float(input("enter the feranit "))
cel=(fah - 32) * 5/9

print("fah=",round(fah,2))
print("cel=",round(cel,2))
#different way to print with round or without round functiom
print("fah=%.2f"%fah)
print("cel=%.2f"%cel)
#different way to print with round or without round functiom
print("fah= %.2f cel= %.2f" %(fah,cel))