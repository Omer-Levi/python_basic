"""
Student: Omer levi
ID: 203499090
Assignment no. 3
Program: stats.py
"""

def string_to_list(st):
    lst = st.split(" ")
    for i in range(len(lst)):
       lst[i] = float(lst[i])
    return lst
        

def stats(ls):
    maxi = max(ls)
    mini = min(ls)
    ava = sum(ls) / len(ls)
    ls1 = ls.copy()
    ls1.sort()
    ls2 = ls.copy()
    ls2.sort(reverse = True)
    print("max =", maxi," in location = ",ls.index(maxi)+1,"\nmin =", mini," in location =",ls.index(mini)+1, "\naverage = ",ava)
    if ls1 == ls:
        print('Ascending sortd')
    elif ls2 == ls:
        print('Descending sorted')
    else:
        print('not sorted')
    
    
s = input("enter numbers with space: ")        

l = (string_to_list(s))
stats(l)