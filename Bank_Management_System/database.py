# Database Bank Management

import mysql.connector as sql

mydb = sql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank_management"
)

cursor = mydb.cursor()

def db_query(query, fetch=False):
    cursor.execute(query)
    if fetch:
        return cursor.fetchall()
    return None

def create_customer_table():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers(
                username VARCHAR(20),
                password VARCHAR(20),
                name VARCHAR(20),
                age INTEGER,
                city VARCHAR(20),
                account_number INTEGER,
                status TINYINT(1)
            )

    ''')

mydb.commit()

if __name__ == "__main__":
    create_customer_table()