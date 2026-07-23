import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",          # Change if your MySQL has a password
        database="hostel_security"
    )
    return conn