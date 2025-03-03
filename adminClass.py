"""
File Name: adminClass.py
Purpose: This file defines the Admin class. It also creates functions for adding/viewing students, instructors, and courses
Special Requirements: None
Date Created: December 10th, 2024
Author: Henry Tanguy
Version Number: 1.0
"""

#import modules for file processing
#import instructor and student class to inherit attributes
from instructorClass import Instructor
from studentClass import Student
import csv

#Define Admin class
class Admin(Instructor, Student):
    #Define attributes
    first_name=''
    last_name=''
    
    #Add constructor
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
    
    #Define string method
    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}, Username: {self.username}, Password: {self.password}'
    
    #Define function for adding students in a new .csv file
    def create_students():
        with open('student.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["first_name", "last_name", "username", "password"])#Create column headers
            choice_loop = 'Y'
            while choice_loop == 'Y' or 'y':#Create loop to let user enter as many students as possible
                fn = input('first name: ')
                if fn == '':
                    print('invalid firstname')
                    continue
                ln = input('last name: ')
                if ln == '':
                    print('invalid lastname')
                    continue
                un = input('username: ')
                if un == '':
                    print('invalid username')
                    continue
                pw = input('password: ')
                if pw == '':
                    print('invalid password')
                    continue
                writer.writerow([fn, ln, un, pw]) #Write inputs to new file
                choice_loop = input('add another student? Y/N \n')
                if choice_loop != 'Y':
                    print('Data saved successfully')
                    break
    
    #Function to append the student.csv file when the user wants to add more students
    def add_student_info():
    
        with open('student.csv', 'a',newline='') as file:
            writer = csv.writer(file)

            choice_loop = 'Y'
            while choice_loop == 'Y' :#loop to add as many students as the user would like
                fn = input('first name: ')
                if fn == '':
                    print('invalid firstname')
                    continue
                ln = input('last name: ')
                if ln == '':
                    print('invalid lastname')
                    continue
                un = input('username: ')
                if un == '':
                    print('invalid username')
                    continue

                pw = input('password: ')
                if pw == '':
                    print('invalid password')
                    continue

                writer.writerow([fn, ln, un, pw])
                choice_loop = input('add another student? Y/N \n')

                if choice_loop != 'Y':
                    print('Data saved successfully')
                    break

    #Function to create the instructor .csv file
    def create_instructor_info():
        with open('instructor.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["first_name", "last_name", "username", "password", 'title']) #create the column headers
            choice_loop = 'Y'
            while choice_loop == 'Y' or 'y':
                fn = input('first name: ')
                if fn == '':
                    print('invalid firstname')
                    continue
                ln = input('last name: ')
                if ln == '':
                    print('invalid lastname')
                    continue
                un = input('username: ')
                if un == '':
                    print('invalid username')
                    continue
                pw = input('password: ')
                if pw == '':
                    print('invalid password')
                    continue
                title = input('Instructor Title: ')
                if title == '':
                    print('invalid title')
                    continue

                choice_loop = input('add another instructor? Y/N \n')
                writer.writerow([fn, ln, un, pw, title])

                if choice_loop == 'N':
                    print('Data saved successfully')
                    break

    #Function to append the instructor.csv file
    def add_instructor_info():
        with open('instructor.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            choice_loop = 'Y'
            while choice_loop == 'Y' or 'y':
                fn = input('first name: ')
                if fn == '':
                    print('invalid firstname')
                    continue
                ln = input('last name: ')
                if ln == '':
                    print('invalid lastname')
                    continue
                un = input('username: ')
                if un == '':
                    print('invalid username')
                    continue

                pw = input('password: ')
                if pw == '':
                    print('invalid password')
                    continue

                title = input('Instructor Title: ')
                if title == '':
                    print('invalid title')
                    continue

                choice_loop = input('add another instructor? Y/N \n')
                writer.writerow([fn, ln, un, pw, title])

                if choice_loop == 'N':
                    print('Data saved successfully')
                    break

    #Funtion to create course list 
    def create_course_list():
        with open('course.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['course_number', 'course_title', 'instructor_name',])#create column headers
            choice_loop = 'Y'
            while choice_loop == 'Y' or 'y':
                cn = input('Enter Course Number: ')
                if cn == '':
                    print('invalid firstname')
                    continue
                ct = input('Enter Course Title: ')
                if ct == '':
                    print('invalid lastname')
                    continue
                #Display the available instructors to choose for the course
                with open('instructor.csv', 'r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in file:
                        print(row)
                    inst_name = input('Please choose an instructor from the list: ')
                    if inst_name == '':
                        print('invalid username')
                        continue

                choice_loop = input('add another course? Y/N \n')
                writer.writerow([cn, ct, inst_name])
                if choice_loop == 'N':
                    print('Data saved successfully')
                    break

    #Function to append the course.csv file
    def add_course_list():
        with open('course.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            choice_loop = 'Y'
            while choice_loop == 'Y' or 'y':
                cn = input('Enter Course Number: ')
                if cn == '':
                    print('invalid firstname')
                    continue
                ct = input('Enter Course Title: ')
                if ct == '':
                    print('invalid lastname')
                    continue

                #Display the available instructors to choose for the course
                with open('instructor.csv', 'r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in file:
                        print(row)
                    inst_name = input('Please choose an instructor from the list: ')
                    if inst_name == '':
                        print('invalid username')
                        continue
                choice_loop = input('add another course? Y/N \n')
                writer.writerow([cn, ct, inst_name])
                if choice_loop == 'N':
                    print('Data saved successfully')
                    break
