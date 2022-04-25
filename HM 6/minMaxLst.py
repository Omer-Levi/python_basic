# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 17:56:25 2021

@author: omerl
"""
import random as rd


def func(lst,size,mini,maxi):
    for i in range(size+1):
        r = rd.randint(mini,maxi)
        lst.append(r)
    return lst

def main():
    lst = []
    size = int(input('How many elements?: '))
    mini = int(input('Min value: '))
    maxi = int(input('Miס value: '))
    print(func(lst,size,mini,maxi))

main()