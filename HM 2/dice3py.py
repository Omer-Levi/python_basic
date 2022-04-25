"""
Student: Omer Levi
ID: 203499090
Assignment no. 2
Program: dice3.py
"""
import random
n = int(input('Please enter n: '))
k = int(input('Please enter k: '))
counter = 0
win = k

while n != 0:
    kube1=random.randint(1, 6)
    kube2=random.randint(1, 6)
    kube3=random.randint(1, 6)
    print(kube1,kube2,kube3)
    if kube1 == kube2 == kube3:
        k-=1
    if k >= 0:
        if k == 0:
            k-=1
        counter +=1
    n-=1
    
if k <= 0:
    print('Reached',win,'equal series after',counter,'games')
else:
    print('you faild')    