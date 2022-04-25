# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 18:23:05 2021

@author: omerl
"""

def revers(mila):
    st = mila.split()
    st.reverse()
    for i in st:
        print(i, end= ' ')
        
def main():
    m = input('Please enter a sentence: ')
    revers(m)

main()
        
        