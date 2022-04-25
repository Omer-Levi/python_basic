# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 18:37:49 2021

@author: omerl
"""


def listi(lst,num):
    ls = [int(d) for d in lst.split()]
    s= []
    for i in ls:
        if i%num !=0:
            s.append(i)
        else:
            continue
    print(s)

def main():
    x=input('Please enter a list of numbers: ')
    y=int(input('Please enter a divaidor: '))
    listi(x,y)

main()
    