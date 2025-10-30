import sqlite3

# Connect to database (creates one if it doesn’t exist)
conn = sqlite3.connect('data.db')

# Create a cursor (to run SQL commands)
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
''')

# Insert sample data
cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Atul', 'atul@example.com'))
cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('John', 'john@example.com'))

# Save (commit) changes and close connection
conn.commit()
conn.close()

print("Database created and sample data added successfully!")
