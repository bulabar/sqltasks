import sqlite3

con = sqlite3.connect("firstDB.db")
cursor = con.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS workers  (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    salary INTEGER 
                )''')

workers = [("Ладюша", 18, 400), ("Дилярушка", 17 ,500), ("Лейладжон", 14, 500)]
cursor.executemany("INSERT INTO workers (name, age, salary) VALUES (?, ?, ?)", workers)
cursor.execute("SELECT * FROM workers")
print(cursor.fetchall())
