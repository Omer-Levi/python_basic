
"""
Created on Fri Jun 11 15:46:04 2021

@author: omerl
"""

def string_to(st):
    st = st.split()
    for i in range(len(st)):
        st[i] = int(st[i])
    return st
        
def average(st):
    count = 0
    for i in range(len(st)):
        count += st[i]
    print(f"the average: {count/len(st)}")

def maxmin(st):
    maxi = max(st)
    mini = min(st)
    x = st.index(maxi)
    y = st.index(mini)
    print(f'tha maximum valu: {maxi} in index: {x+1}')
    print(f'tha minium valu: {mini} in index: {y+1}')
    
def yored(st):
    x = st.copy()
    y = st.copy()
    x.sort()
    y.sort(reverse=True)
    if x == st:
        print('The numbers in the series are rising')
    elif y == st:
        print('The numbers in the series are going down')
    elif y != st or x != st:
        print('eror')

            
def main():
    number = input('input number: ')
    st = string_to(number)
    average(st)
    maxmin(st)
    yored(st)

main()    
    
    
    
    