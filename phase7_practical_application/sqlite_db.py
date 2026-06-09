import sqlite3
connection = sqlite3.connect("company.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                (id INTEGER PRIMARY KEY, name TEXT, role TEXT)''')
cursor.execute("INSERT INTO employees (name, role) VALUES (?, ?)", (""
"charan", "Manager"))
connection.commit()

#this one is just for practice
cursor.execute("SELECT * FROM employees")
employees = cursor.fetchall()
for emp in employees:
    print(emp)
#until here

connection.close()