import sqlite3
import bcrypt

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    password BLOB
)
""")

conn.commit()

def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    cursor.execute(
        "INSERT INTO users VALUES (?, ?)",
        (username, hashed)
    )

    conn.commit()
    print("Registration Successful")

def login():
    username = input("Username: ")
    password = input("Password: ")

    cursor.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )

    result = cursor.fetchone()

    if result:
        if bcrypt.checkpw(password.encode(), result[0]):
            print("Login Successful")
        else:
            print("Invalid Password")
    else:
        print("User Not Found")

while True:
    print("\n1.Register")
    print("2.Login")
    print("3.Exit")

    choice = input("Choose: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        break

conn.close()