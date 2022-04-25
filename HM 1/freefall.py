"""
Student: Omer Levi
ID: 203499090
Assignment no. 1
Program: freefall.py
"""
h = float(input("What is the height of the stone fall?: "))
g = 9.8 #Meters per second **2
t = ((2*h/g)**0.5) #Fall time
v = g*t
print("Falling time:",t,"Seconds")
print("Falling speed:",v,"Meters per second")
 