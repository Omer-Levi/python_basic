"""
Student: Omer Levi
ID: 203499090
Assignment no. 1
Program: quadratic.py
"""
a = float(input("Enter first parameter (a): "))
b = float(input("Enter second parameter (b): "))
c = float(input("Enter third parameter (c): "))
xx = b**2 - 4*a*c #xx = Discriminant
if xx < 0:
    print("No solution")
elif xx > 0:
    print("Two solution",-b+xx**0.5//2*a , -b-xx**0.5//2*a) 
else:
    print("One solution", -b//2*a)
    
d = 10
while d >0:
    print(d)     