import psycopg2

conn = psycopg2.connect(host="localhost", dbname="test_db",
                        user="poe", password="#####", port=5433)
cur = conn.cursor()

cur.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR
        );
    """)

cur.execute("""
    INSERT INTO customer (id, name, age, gender) VALUES
    (1, 'Mike', 26, 'M'),
    (2, 'Nicole', 35, 'F'),
    (3, 'John', 25, 'M'),
    (4, 'Amina', 26, 'F'),
    (5, 'Bob', 30, 'M');
""")

# To fetch just one data we want
cur.execute("""
    SELECT * FROM customer WHERE name='John';
 """)
print(cur.fetchone())


# To fetch all records
cur.execute("""
    SELECT * FROM customer WHERE age<= 30;
 """)
for record in cur.fetchall():
    print('all records of age >= 30',record)

#####################################################################################

cur.execute("""
        CREATE TABLE IF NOT EXISTS book (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            release_date DATE,
            cost INT
        );
    """)

cur.execute("""
    INSERT INTO book (id, name, release_date, cost) VALUES
    (1, 'Hello', '2024-10-10', 5000),
    (2, 'World', '2023-11-10', 6000),
    (3, 'Peace', '2022-08-10', 8000),
    (4, 'Soft', '2024-03-10', 9000),
    (5, 'Beauty', '2024-10-25', 12000);
""")

sql = cur.mogrify("""SELECT * FROM book WHERE starts_with(name, %s) AND cost > %s;""", ("B", 9000))
print("sql:", sql)

cur.execute(sql)
print("fetch_all:", cur.fetchall())

conn.commit()
cur.close()
conn.close()