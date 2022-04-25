"""
Student: Omer Levi
ID: 203499090
Assignment no. 2
Program: decSeries.py
"""

numbers = int(input('input num of numbres: ')) #number of elemnts
num = int(input('input nummber: ')) #elemnts in the series
counte = 1
countemax = 0
maxi = num


for index in range(numbers-1): #if index in numbers enter the "for"
    if num < maxi:
        counte += 1
        maxi = num
    else:
        countemax = counte
        counte = 1
        maxi = num
    num = int(input('input nummber: '))
    
print('Number of elements in the series :',countemax,)   #print who muthe number in series   