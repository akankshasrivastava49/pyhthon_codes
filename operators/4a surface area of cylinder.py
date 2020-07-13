# 4 write a program to compute surface area of cylinder
pi = 3.14
r = float(input("enter radius:"))
h = float(input("enter height:"))
surface_area = 2*pi*r*h + 2*pi*r**2
print("surface area of cylinder",surface_area)