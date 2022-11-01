#!/bin/python3
#coding: UTF8
import mysql.connector
from mysql.connector import Error

try:
    dbconnection = mysql.connector.connect(host="192.168.56.101",
                                           database="py_db",
                                           user="py_user",
                                           password="1234qwerQW")

    if dbconnection.is_connected():
        db_Info = dbconnection.get_server_info()
        print("Connected to MySQL Server version", db_Info)
        dbcursor = dbconnection.cursor()

        # mysqlQuery = (""" SELECT * FROM first; """)

        dbcursor.execute("select database();")
        record = dbcursor.fetchone()
        print("You're connected to dataserver: ", record)

        mysqlQuery = ("SELECT * FROM first WHERE id=6;")
        dbcursor.execute(mysqlQuery)
        record = dbcursor.fetchone()
        print("Some part of database: ", record)

        mysqlQuery = ("SELECT * FROM first;")
        dbcursor.execute(mysqlQuery)
        record = dbcursor.fetchall()
        print("Some part of database: ", record)

        mySql_Create_Table = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

        dbcursor = dbconnection.cursor()
        result = dbcursor.execute(mySql_Create_Table)
        print("Laptop table was created.") 

except Error as e:
    print("Error while connected to database: ", e)
finally:
    if dbconnection.is_connected():
        dbcursor.close()
        dbconnection.close()
        print("MySQL connection is closed!")

