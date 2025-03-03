"""
File Name: studentExecutable.py
Purpose: This file will prompt the user for log in information from the student.csv file.
After a successful log in, the student main menu will be displayed.
The user will be prompted to select an option from the menu and enter the required information.
Special Requirements: None
Date Created: December 10th, 2024
Author: Henry Tanguy
Version Number: 1.0
"""

#Import modules for log in and file processing, as well as the student Class
import utility
import os
from studentClass import Student

#Define the source file for log in information
SourceFile = 'student.csv'

#Function to return to the student main menu
def return_to_menu():
    menu_loop = input('Return to Main Menu? (Y/N) \n')
    if menu_loop == 'Y':
        student_main_menu()
    else:
        print('exiting program')

#Define main function for student to use
def student_main_menu():
    
    if utility.user_verified == True:
        print('\n-----------Main Menu-----------')
        print('1. Enroll in a course')
        print('2. View Enrolled courses')
        print('3. Exit')
        choice = int(input('Please select an option: \n'))

        if choice < 1:
            print('Option unavailable. Please select an option from 1-3')
        else:
            if choice > 3:
                print('Option unavailable. Please select an option from 1-3')
            else:
                if choice == 1:
                    if os.path.isfile('course.csv'):
                        Student.enroll()
                        return_to_menu()
                    else:
                        print('No information has been entered. Please try again later.')
                        return_to_menu()
                else:
                    if choice == 2:
                        if os.path.isfile('enrollment.csv'):
                            utility.view_info('enrollment.csv')
                            return_to_menu()
                        else:
                            print('No information has been entered. Please try again later.')
                            return_to_menu()
                    else:
                        if choice ==3:
                            print('Exiting program')
                        
#Call functions to load student data, log in, and run main menu
utility.load_user_data(SourceFile)
utility.login(SourceFile)
student_main_menu()