import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="pa$$word",database="Annadata_Sukhibava")

mycursor=mydb.cursor()

mycursor.execute("create table PESTICIDES_USED(SNO varchar(5) primary key,ID varchar(5),DATE_OF_QUERY varchar(10),PESTICIDE varchar(1000))")
