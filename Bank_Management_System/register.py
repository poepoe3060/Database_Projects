# User Registration Sign In & Sign Up

from database import *
def SignUp():
    username = input("Create Username: ")
    temp = cursor.execute(f"SELECT username FROM customers WHERE username = '{username}';")
    print("Username", temp)