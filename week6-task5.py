# -*- coding: utf-8 -*-
"""
Created on

@author: 
    
"""

password = "changeme"

passw = " "
count = 0
while(password != passw):
    passw = input("Enter the password : ")
    count += 1
    if password == passw:
        print("Accepted")
        break;
    if count == 5:
        print("Access denied, please press enter to exit and contact security to reset your password")
        break;
print("Number of attempts: ", count)
