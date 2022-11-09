# Company Name: MariaClara Solutions
# Developer Name: Rodel
# Date: November 10, 2022

import os

os.system("clear")

##############################
# DATA TYPES
# String
# Number (int and decmimal)
# List - immutable
# Tuples - mutable
# Dictionaries
# Boolean - True or False
##############################


employee_name = "John"
age = 41
employee_list = ["John", "Mary", "Bob", "Joseph", 365]
employee_tuples = ("John", "Mary", "Bob", "Joseph", 365)

employee_department = {
    "John": "Finance", 
    "Mary": "Accounting",
    "Bob": "IT"
    }

is_active = True

print("Hello " + employee_name)
print("This is my Emp-List: " + str(employee_list))
print("This is my Emp-Tuples: " + str(employee_tuples))
print("This is my EmpDept-Dict : " + str(employee_department))
print("*" * 50)
print("John is under " + employee_department['John'] + " department.")
print("John is active employee? " + str(is_active))

print()


