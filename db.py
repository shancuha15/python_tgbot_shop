import sqlite3


# Create a database table.
with sqlite3.connect("botusers.db") as db:
    cursor = db.cursor()

    cursor.executescript("""CREATE TABLE IF NOT EXISTS dbusers(
                        id integer PRIMARY KEY,
                        user_id text NOT NULL,
                        user_name text NOT NULL,
                        user_surname text ,
                        username text NOT NULL
                        );""")
    db.commit()

conn = sqlite3.connect('botusers.db', check_same_thread=False)
cursor = conn.cursor()
users = []


# This function adds user information to the database.
def db_table_add(user_id: int, user_name: str, user_surname: str, username: str):
    a = str(user_id)
    if a + '\n' not in users:
        file = open('user_list.txt', 'a')
        cursor.execute('INSERT INTO dbusers (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                       (user_id, user_name, user_surname, username))
        file.write(a + '\n')
        file.close()
        conn.commit()


# This function reads the user ID and adds it to the list for further use.
def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    f = open('user_list.txt')
    for row in f:
        users.append(row)
    f.close()
    db_table_add(user_id, user_name, user_surname, username)
