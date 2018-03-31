# -*- coding: utf-8 -*-
"""
Created on 

@author: 
"""

def prnpage(page):
    if page % 2 == 0:
        return True
    else:
        return False


def main():
    page = int(input("Enter the page num: "))
    
    result = prnpage(page)
    if result == True:
        print(page)
    else:
        print("%60s%d" % (" ", page))
    
main()
