# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:31:43 2021

@author: omerl
"""
num = int(input('input number, for brake inpuyt "0": '))  
st = []
count = 0
nel = 0

while num != 0:
    st.append(num)
    count +=num
    nel +=1    
    num = int(input('input number, for brake inpuyt "0": '))  
else:
      print(f'average = {count/nel}')  
      print(f'max value is {max(st)} in cell {st.index(max(st))+1}')
      print(f'min value is {min(st)} in cell {st.index(min(st))+1}')

        
        