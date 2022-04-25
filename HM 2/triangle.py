"""
Student: Omer Levi
ID: 203499090
Assignment no. 2
Program: triangle.py
"""

h = int(input('Enter height: ')) #9
d = int(input('Enter number of $: ')) #5
s = int(input('Enter number of spaces: '))#2

dolar = d
spe = s

if h < 2:
    print('Eror, Enter heigh')
else:    
    print(" "*(h-1)+"*")
    
    for i in range(h-2):
        for j in range(h-i-2):
            print(' ',end='')
        print('*',end='')
        for k in range(1+2*i):
            if d:
                print("$",end="")
                d -=1
            else:
                if s:
                    print(' ',end='')
                    s -=1
            if s==0 and d==0:
             s = spe
             d = dolar
        print('*')
    print('*'*(h*2-1))     
             