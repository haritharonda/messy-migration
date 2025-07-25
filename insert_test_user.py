import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE email = ?", ("haritha@example.com",))
existing_user = cursor.fetchone()

if not existing_user:
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Haritha", "haritha@example.com"))
    conn.commit()
    print("User inserted.")
else:
    print("User already exists.")

conn.close()


