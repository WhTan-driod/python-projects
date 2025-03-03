"""
File Name: studentClass.py
Purpose: This file contains the student Class object
Special Requirements: None
Date Created: December 10th, 2024
Author: Henry Tanguy
Version Number: 1.0
"""

#Import user object and csv module for file processing
from userClass import User
import csv

#Define class
class Student(User):
    first_name=''
    last_name=''
    
    #Define constructor
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    #Define string method
    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}, Username: {self.username}, Password: {self.password}'
    
    #Define function to enroll in a previously entered course from the adminExecutable file
    def enroll():
        with open('course.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
        enrollment_choice = int(input('Please select a class number to enroll: \n'))
        with open('enrollment.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([enrollment_choice, Student.username])