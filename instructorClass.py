"""
File Name: instructorClass.py
Purpose: This file defines the instructor class
Special Requirements: None
Date Created: December 10th, 2024
Author: Henry Tanguy
Version Number: 1.0
"""
#Import the user class to be inherited by the instructor class
from userClass import User

#Define Instructor class
class Instructor(User):
    first_name=''
    last_name=''
    
    #Define constructor
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
    
    #Define string method
    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}, Username: {self.username}, Password: {self.password}'
    
    #Define setters
    def set_first_name(s, fn):
        s.first_name = fn

    def set_last_name(s, ln):
        s.last_name = ln

    #Define getters
    def get_name(s):
        return s.first_name + s.last_name
    