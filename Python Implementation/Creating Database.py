import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="pa$$word")

mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE Annadata_Sukhibava")
