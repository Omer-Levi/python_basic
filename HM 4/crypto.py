"""
Student: omer levi
ID: 203499090
Assignment no. 4
Program: crypto.py
"""

import random

def key():  #Random Encryption Key Function
    st = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    random.shuffle(st)
    k = open('key.txt', 'w')
    for elemnts in st:
        k.write(elemnts)
    k.close()

def dictionary():  #Text encryption function
    k = open('key.txt', 'r')  #Open the text file
    st = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    d = {}   #Create a dictionary
    for i in range(len(st)):
        d[st[i]] = k.read(1)
    k.close()
    return d    
    
    
def encrypt():   
    d = dictionary() #Call to function
    f = open('plaintext.txt', 'r')  #Open the text file
    c = open('ciphertext.txt', 'w')   #Open the text file  
    for line in f:
        for character in line:
            if character.isalpha():
                character.lower()
                c.write(d[character])
            else:
                c.write(character)
    f.close()
    c.close()
    
def decrypted():
    d = dictionary()
    v_lst = list(d.values())
    k_lst = list(d.keys())
    f = open('decrypted.txt', 'w')
    c = open('ciphertext.txt', 'r')
    for line in c:
        for character in line:
            if character.isalpha():
                character.lower()
                pos = v_lst.index(character)
                f.write(k_lst[pos])
            else:
                f.write(character)
    f.close()
    c.close()            
                
def main():
    while True:
        case = input('Enter "k" to the Key, Enter "e" to the Encrypt, enter "d" to the Decrypted: ')
        if case == "k":
            key()
        elif case == "e":
            encrypt()
        elif case == "d":
            decrypted()
        else:
            print('sorry, good bye')
            return
            
main()




















