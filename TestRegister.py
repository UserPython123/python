# -*- coding: utf-8 -*-
"""
Created on 

@author: 
"""

from cashregister import cashRegister

def main():
    
    cashReg = cashRegister()
    price=1
    print("Enter 0 to stop adding items...")
    while price!= 0:
        price = float(input("Enter price of the new item to be added: "))
        if price != 0:
            cashReg.addItem(price)
    
    totalPrice = cashReg.getTotal()
    itemCount = cashReg.getCount()
    
    print("Total price: ", totalPrice)
    print("Item count: ", itemCount)
    
main()

    
