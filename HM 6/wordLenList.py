# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 19:29:39 2021

@author: omerl
"""

def word(s,w):  #the quick brown fox jumps over the lazy dog"
    x=s.split()
    ls = []
    for i in x:
        if w != i:
            ls.append(len(i))
        else:
            continue
    print(f'output {ls}')
    
def main():
    word("the quick brown fox jumps over the lazy dog", "the")
            
        
main()