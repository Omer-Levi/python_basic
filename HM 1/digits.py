"""
Student: Omer Levi
ID: 203499090
Assignment no. 1
Program: digits.py
"""

num = int(input("Enter a 4-digit number: "))
if len(str(num)) !=4: 
    print("Error: Please enter 4 digits.")
else:
    x = num % 10 # X=num R side
    num = num //10
    y = num % 10 # Y=num M-R side
    num = num //10
    z = num % 10 # Z=num M-L side
    num = num //10
    q = num % 10 # Q=num L side

    print(x,y,z,q)
    print("     ",x)
    print("   ",y)
    print(" ",z)
    print(q)
    print(q,z,y,x)




    