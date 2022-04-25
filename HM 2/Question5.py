"""
Student: Omer Levi
ID: 203499090
Assignment no. 2
Program: Question5.py
"""

mel = input('Please enter a sentence: ')
st = mel.split() #Splits the sentence

for i in st:
    print(i)
print(f'There are {len(st)} words in: {mel}')