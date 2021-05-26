import sqlite3

connection  =sqlite3.connect('data.db')

cursor = connection.cursor()

create_table =  "CREATE TABLE users (id int, username tect, password text)"

cursor.execute(create_table)

user  =(1, 'bob', 'asdf')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'
cursor.execute(insert_query, user)

users = [
    (2, 'jose', 'xyz'),
    (3, 'rolf', 'xyas')
]

cursor.executemany(insert_query, users)


select_query = "SELECT * from users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()