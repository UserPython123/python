# -*- coding: utf-8 -*-
"""
Created on 

@author:
"""

from student import student

def main():
    
    Surname = input("Enter student's surname: ")
    Firstname = input("Enter student's first name: ")
    StuNo = input("Enter student number: ")
    Course = input("Enter student's course: ")
    
    stuObj = student(Surname,Firstname,StuNo, Course)
    
    print("Initial details...",stuObj)
    
    print("Change Surname...")
    Surname = input("Enter new surname: ")
    
    stuObj.set_Surname(Surname)

    print("Change course...")
    Course = input("Enter the name for new course: ")
    stuObj.set_Course(Course)

    print("Updated student details...",stuObj)
    
main()

    
    
