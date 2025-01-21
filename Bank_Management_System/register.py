# User Registration Sign In & Sign Up

import random
from database import *

def SignUp():
    username = input("Create Username: ")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        print("Username already exits!")
        SignUp()
    else:
        print("Username is available, Please proceed")
        password = input("Enter your acc password: ")
        name = input("Enter your Name: ")
        age = input("Enter your Age: ")
        city = input("Enter your City: ")
        while True:
            account_number = random.randint(10000000, 99999999)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                break

if __name__ == '__main__':
    SignUp()