"""
File Name: utility.py
Purpose: This file contains generic functions to be used in the executable files for log in control and displaying information from .csv files
Special Requirements: None
Date Created: December 10th, 2024
Author: Henry Tanguy
Version Number: 1.0
"""

import csv
user_verified = False

def load_user_data(csv_file):
    user_dict = {}  # Initialize an empty dictionary to store users

    # Open and read the CSV file
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)  # Use csv.reader to read the file row by row

        # Skip the header row (if it exists)
        next(reader)

        # Loop through each row in the CSV file (after the header)
        for row in reader:
            try:
                first_name, last_name, username, password = row

                # Store user information in the dictionary with username as the key
                user_dict[username] = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'password': password
                }
            except:
                first_name, last_name, username, password, title = row

                # Store user information in the dictionary with username as the key
                user_dict[username] = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'password': password,
                    'Title': title
                }

    return user_dict

# Function to check login credentials
def login(csv_file):
    # Load the user data from the CSV file
    users = load_user_data(csv_file)
    global user_verified
    max_attempts = 3
    attempts = 0

    # Prompt the user for their username and password
    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if the username exists
        if username in users:
            # Check if the password matches
            if users[username]['password'] == password:
                print(f"Login successful! Welcome {users[username]['first_name']} {users[username]['last_name']}.")
                user_verified = True
                break
                
            else:
                print("Invalid username or password. Please try again.")
                attempts += 1
        else:
            print('Invalid username or password. Please try again')
            attempts += 1
        if attempts == 3:
            print('You have reached the maximum number of attempts. Please try again later.')

#Define generic function to display a files contents
def view_info(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

