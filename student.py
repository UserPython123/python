# -*- coding: utf-8 -*-
"""
Created on 

@author: 
"""

class student:
    def __init__(stu, surname, firstname, stunum, course):
        stu.surname = surname
        stu.firstname = firstname
        stu.stunum = stunum
        stu.course = course
    
    def get_Surname(stu):
        return stu.surname
    
    def set_Surname(stu,surname):
        stu.surname = surname
    
    def get_Firstname(stu):
        return stu.firstname
    
    def set_Firstname(stu,firstname):
        stu.firstname = firstname
    
    def get_Studentnumber(stu):
        return stu.stunum
    
    def set_Studentnumber(stu, stunum):
        stu.stunum = stunum
    
    def get_Course(stu):
        return stu.course
    
    def set_Course(stu,course):
        stu.course = course
        
    def __str__(stu):
        return "Surname: %s \t FirstName: %s \t  Student number: %s \t Course taken: %s " % (stu.surname, stu.firstname, stu.stunum, stu.course)


    
    
