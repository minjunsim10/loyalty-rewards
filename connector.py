'''import mysql.connector

# Connect to the existing database 'loyaltydb'
db = mysql.connector.connect(
    host="localhost",        # Host where your MySQL server is running
    user="mj",             # Your MySQL username
    passwd="root",           # Your MySQL password
    database="mydb"     # The name of the existing database
)

mycursor = db.cursor()

# Example: Check if connection is successful
print("Connected to mydb database!")

# Example: Show all tables in the connected database
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)


mycursor.execute("SHOW TABLES")
print("Tables in the database:")
for table in mycursor:
    print(table)'''
