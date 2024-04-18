import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS employees (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         department TEXT
#     )
# ''')

conn.commit()
