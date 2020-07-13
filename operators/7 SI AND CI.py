# 7 Write a program to compute simple interest and compound interest
p = float(input("enter principle:"))
r = float(input("enter rate:"))
t = float(input("enter time:"))

simple_interest=( p * r * t)/100
compound_interest = p * (pow((1 + r / 100), t))

print("simple interest is ",simple_interest )
print("compound interest is ",compound_interest )
