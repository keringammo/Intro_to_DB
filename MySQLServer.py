#!/usr/bin/python3
"""
This script connects to a MySQL server and creates the database 'alx_book_store'.
If the database already exists, the script will not fail.
"""

import mysql.connector
from mysql.connector import Error

try:
    # Connect to the MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",          # 🔹 Replace with your MySQL username
        password="yourpassword"   # 🔹 Replace with your MySQL password
    )

    # Create a cursor object to execute SQL commands
    mycursor = mydb.cursor()

    # Create the database if it doesn't already exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except Error as e:
    # Handle connection or SQL errors
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close the cursor and database connection properly
    if mycursor:
        mycursor.close()
    if mydb.is_connected():
        mydb.close()
        print("MySQL connection closed.")
