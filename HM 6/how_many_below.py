# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 19:05:46 2021

@author: omerl
"""

def multi(lst1,lst2):
    ls = []
    for i in range(len(lst1)):
        ls.append(lst1[i]*lst2[i])
    print(ls)


def how(arr,hold):
    c = 0
    for i in arr:
        if i<hold:
            c+=1
        else:
            continue
    print(f'Output: {c}')

def main():
    multi([1,2,7],[5,4,7])
    how([1,2,4,5,7,8,9,7,5,2,1,4,5,3,0],5)
main()
