"""
File Name: userClass.py
Purpose: This file contains the user class object
Special Requirements: None
Date Created: December 10th, 2024
Author: Henry Tanguy
Version Number: 1.0
"""

#Defin the user class
class User:
    username=''
    password=''

    #Define the constructor
    def __init__(self,un,pw):
        self.username = un
        self.password = pw

    #Define the string method
    def __str__(self):
        return f'Username: {self.username}, Password {self.password}'

    #Define the setter methods
    def set_username(s, un):
        s.username = un

    def set_password(s, pw):
        s.password = pw

    #Define the getter methods
    def get_username(s):
        return s.username

    def get_password(s):
        return s.password