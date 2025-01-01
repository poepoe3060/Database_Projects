import psycopg2

conn = psycopg2.connect(host="localhost", dbname="bank_management_system",
                        user="sai", password="sai", port=5433)
cur = conn.cursor()

cur.execute("""
        CREATE TABLE IF NOT EXISTS person (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR
        );
    """)

cur.execute("""
    INSERT INTO person (id, name, age, gender) VALUES
    (1, 'Mike', 26, 'M'),
    (2, 'Nicole', 35, 'F'),
    (3, 'John', 25, 'M'),
    (4, 'Amina', 26, 'F');
""")
conn.commit()
cur.close()
conn.close()