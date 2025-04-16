import math as m
a = int(input("length in feet"))
b = int(input("angle in degree"))
b1 = (((m.pi)/180)*b)
height = a*m.sin(b1)
print(int(round(height,2)))