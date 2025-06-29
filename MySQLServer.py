import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (without specifying a database)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''  # Change if you have a password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")
except mysql.connector.Error

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
