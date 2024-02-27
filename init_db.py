import sqlite3

# Establish a connection to the SQLite database (creating it if it doesn't exist)
connection = sqlite3.connect('database.db')

# Open and execute the schema.sql file to create the necessary table(s)
with open('schema.sql') as f:
    connection.executescript(f.read())

# Create a cursor to execute SQL commands
cur = connection.cursor()

# Insert sample data into the 'posts' table
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post'))

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post'))

# Commit the changes to the database
connection.commit()

# Close the database connection
connection.close()
