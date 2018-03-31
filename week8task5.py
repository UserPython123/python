# -*- coding: utf-8 -*-
"""
Created on 

@author: 
"""

def countSpace(sentence):
    spaceCount = 0
    for character in sentence :
        if character == " ":
            spaceCount += 1
    return spaceCount

def main():
    
    sentence = input("Enter sentence:")
    
    spaceCount = countSpace(sentence)
    
    print("There are ", spaceCount," spaces.")

main()


    
