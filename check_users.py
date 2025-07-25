import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

users = cursor.execute("SELECT * FROM users").fetchall()

print("Users in DB:")
for user in users:
    print(user)

conn.close()
