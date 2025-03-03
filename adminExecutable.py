"""
File Name: adminExecutable
Purpose: This file will prompt the user for log in information from the admin.csv file.
After a successful log in, the admin main menu will be displayed.
The user will be prompted to select an option from the menu and enter the required information.
Special Requirements: None
Date Created: December 10th, 2024
Author: Henry Tanguy
Version Number: 1.0
"""

#Import modules for file processing, utility functions, and object class
import os
import utility
from adminClass import Admin

#Declair variable for log in function
SourceFile = 'admin.csv'

#Define function for menu looping
def return_to_menu():
    menu_loop = input('Return to Main Menu? (Y/N) \n')
    if menu_loop == 'Y':
        admin_main_menu()
    else:
        print('exiting program')

#Define function to display menu
def admin_main_menu():

    #Funtion only runs if log in is successful
    if utility.user_verified == True:

        #List options
        print('\n-----------Main Menu-----------')
        print('1. Add Student')
        print('2. Add Instructor')
        print('3. Add Course')
        print('4. View Students')
        print('5. View Instructors')
        print('6. View Courses')
        print('7. View Enrollment')
        print('8. Exit\n')
        choice = int(input('Please select one option\n'))


        #If/else structor to call the appropriate function depending on the users selection
        if choice < 1:
            print('Option unavailable. Please select an option from 1-7')
        else:
            if choice > 8:
                print('Option unavailable. Please select an option from 1-7')
            else:
                if choice == 1:
                    if os.path.isfile('student.csv'):
                        Admin.add_student_info()
                        return_to_menu()
                    else:
                        Admin.create_students()
                        return_to_menu()
                else:
                    if choice == 2:
                        if os.path.isfile('instructor.csv'):
                            Admin.add_instructor_info()
                            return_to_menu()
                        else:
                            Admin.create_instructor_info()
                            return_to_menu()
                    else:
                        if choice == 3:
                            if os.path.isfile('course.csv'):
                                Admin.add_course_list()
                            else:
                                Admin.create_course_list()
                                return_to_menu()
                        else:
                            if choice == 4:
                                if os.path.isfile('student.csv'):
                                    utility.view_info('student.csv')
                                    return_to_menu()
                                else:
                                    print('No data has been entered. Please try again later.')
                                    return_to_menu()
                            else:
                                if choice == 5:
                                    if os.path.isfile('instructor.csv'):
                                        utility.view_info('instructor.csv')
                                        return_to_menu()
                                    else:
                                        print('No data has been entered. Please try again later.')
                                        return_to_menu()
                                else:
                                    if choice == 6:
                                        if os.path.isfile('course.csv'):
                                            utility.view_info('course.csv')
                                            return_to_menu()
                                        else:
                                            print('No data has been entered. Please try again later.')
                                            return_to_menu()
                                    else:        
                                        if choice == 7:
                                            if os.path.isfile('enrollment.csv'):
                                                utility.view_info('enrollment.csv')
                                                return_to_menu()
                                            else:
                                                print('No data has been entered. Please try again later.')
                                                return_to_menu()
                                        else:
                                            if choice == 8:
                                                print('Exiting program')
                                                return



#Call the functions to load user data, log in, and run the main admin function.
utility.load_user_data(SourceFile)
utility.login(SourceFile)
admin_main_menu()
