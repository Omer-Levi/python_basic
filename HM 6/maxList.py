# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 19:40:52 2021

@author: omerl
"""

def maxList(lst1, lst2):
    ls = []
    for i in range(len(lst1)):
        if lst1[i] >= lst2[i]:
            ls.append(lst1[i])
        else:
            ls.append(lst2[i])
    print(ls)
    
def main():
    maxList([1,2,4,7,8,2,3],[2,5,4,5,9,6,3])
    
main()