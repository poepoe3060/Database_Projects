# User Registration Sign In & Sign Up
from database import *

if __name__ == '__main__':
    def SignUp():
        username = input("Create Username: ")
        temp = cursor.execute(f"SELECT username FROM customers WHERE username = '{username}';")
        print("Username", temp)