# -*- coding: utf-8 -*-
"""
Created on 

@author: 
"""

def mystery(number) :
    if number <= 0 : 
        return 0
    else:
        return (mystery(number // 2) + 1)


def main():
    number = mystery(25)
    print(number)
main()
