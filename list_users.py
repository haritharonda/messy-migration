import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Comment or remove this line:
# cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Haritha", "haritha@example.com"))

cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

if not users:
    print("No users found.")
else:
    for user in users:
        print(user)

conn.close()


