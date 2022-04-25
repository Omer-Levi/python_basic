# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:53:05 2021

@author: omerl
"""

import random as rd

def dice(n,k):  #(5,2)
    t = 0
    for i in range(n):
        dice_1 = rd.randint(1,6)
        dice_2 = rd.randint(1,6)
        dice_3 = rd.randint(1,6)
        print(f'{dice_1}, {dice_2}, {dice_3}')
        count = 0
        t += 1
        if dice_1 == dice_2 == dice_3:
            count += 1    
    print(f'Reached {count} equal series after {(t-count)} games')
            
    
def main():
    n = int(input('Please enter chense: '))
    k = int(input('Please enter win: '))
    return dice(n,k)

main()