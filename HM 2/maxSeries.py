"""
Student: Omer Levi
ID: 203499090
Assignment no. 2
Program: maxSeries.py
"""
num = int(input("Enter an integer, to stop enter zero: ")) #Enter an integer
sumn = 0 #The sum of the numbers
count = 0 #Number of element
maxi = num #The maximum number
mini = num #The minimum number
m = 0
n = 0

while num:    #Loop entry if number =! 0
    sumn += num
    if num > maxi:
        maxi = num
        m = count
    elif num < mini:
        mini = num
        n = count 
    count += 1     
    num = int(input("Enter an integer, to stop enter zero: "))
    
print('average:', sumn/count)
print("max value is",maxi,"in cell",m+1 )
print('min value is',mini,'in cell' ,n+1)

    