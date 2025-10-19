#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it doesn’t exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: print to confirm closure
            # print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
