import pandas as pd

# Step 1 : import sqlite3 module
import sqlite3

# Step 2 : connect to the database (it will create a 'example.db' file if not exist)
conn = sqlite3.connect("example.db")

# Step 3 : Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Step 4 : Create a table
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT
    )
""")

# Step 5 : Insert some data
cursor.execute(
    "INSERT INTO users (username, email) VALUES(?, ?)",
    ("arbaaz1999", "arbaazmansuri09@gmail.com"),
)
cursor.execute(
    "INSERT INTO users(username, email) VALUES(?, ?)",
    ("moin1992", "mansurimoin05@gmail.com"),
)

# Step 6 : Commit the changes
conn.commit()

# Step 7 : Query the data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

table = pd.read_sql_query("SELECT * FROM users", conn)
table.to_csv("user.csv", index_label="index")

# Step 8 : Display the Data
for row in rows:
    print(row)

# Step 9 : Close the connection
conn.close()
