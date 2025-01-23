# User Registration Sign In & Sign Up

import random
from customers import *
from database import *

def SignUp():
    username = input("Create Username: ")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';", fetch=True)
    if temp:  # Check if results exist
        print("Username already exists!")
        SignUp()
    else:
        print("Username is available, Please proceed")
        password = input("Enter your acc password: ")
        name = input("Enter your Name: ")
        age = input("Enter your Age: ")
        city = input("Enter your City: ")
        while True:
            account_number = random.randint(10000000, 99999999)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';", fetch=True)
            if temp:
                continue
            else:
                print('Account number:', account_number)
                break
    customer_obj = Customer(username, password, name, age, city, account_number)
    customer_obj.createuser()