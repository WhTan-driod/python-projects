"""
File Name: instructorExecutable.py
Purpose: This file will prompt the user for log in information from the instructor.csv file.
After a successful log in, the instructor main menu will be displayed.
The user will be prompted to select an option from the menu and enter the required information.
Special Requirements: None
Date Created: December 10th, 2024
Author: Henry Tanguy
Version Number: 1.0
"""

#Import modules for log in control, file processing, and objects
import utility
import os
from instructorClass import Instructor

#Define source file for log in control
SourceFile = 'instructor.csv'

#function to return to instructor main menu
def return_to_menu():
    menu_loop = input('Return to Main Menu? (Y/N) \n')
    if menu_loop == 'Y':
        inst_main_menu()
    else:
        print('exiting program')

#Define menu function for instructor to use
def inst_main_menu():
    if utility.user_verified == True:
        print('\n-----------Main Menu-----------')
        print('1. View Enrolled courses')
        print('2. Exit')
        choice = int(input('Please select an option: \n'))

        if choice < 1:
            print('Option unavailable. Please select an option from 1-3')
        else:
            if choice > 3:
                print('Option unavailable. Please select an option from 1-3')
            else:
                if choice == 1:
                    if os.path.isfile('enrollment.csv'):
                        utility.view_info('enrollment.csv')
                        return_to_menu()
                else:
                    if choice == 2:
                        print('Exiting program')

    
#Call functions to load user data, log in, and run menu function
utility.load_user_data(SourceFile)
utility.login(SourceFile)
inst_main_menu()