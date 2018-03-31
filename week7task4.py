# -*- coding: utf-8 -*-
"""
Created on 

@author: 
"""

shoppinglist = []
setFlag = 1
item = ""

while(setFlag != 0):
    item = input("Enter the item in shopping list : ")
    if item == "":
        setFlag = 0
        break;
    else:
        shoppinglist.append(item)
print(shoppinglist)

