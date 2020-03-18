#!C:\Users\abhin\AppData\Local\Programs\Python\Python38-32/python
import pymysql
import cgi,cgitb
import os
form = cgi.FieldStorage()
Table_Name    = form.getvalue('Table_Name')
First_Column  = form.getvalue('First_Column')
Second_Column = form.getvalue('Second_Column')
First_Column_Datatype  = form.getvalue('first_col_data_type')
Second_Column_Datatype = form.getvalue('second_col_data_type')
Length1=form.getvalue('Length1')
Length2=form.getvalue('Length2')

# Open database connection
db = pymysql.connect("localhost","root","", database = "bill_info")
# prepare a cursor object using cursor() method
cursor = db.cursor()
# execute SQL query using execute() method.
#str="create table users          ("+First_Column+" char(20),"+Second_Column+" char(20))"
str="create table " +Table_Name+"("+First_Column+" "+First_Column_Datatype+"("+Length1+")"","+Second_Column+" "+Second_Column_Datatype+"("+Length2+"))"

cursor.execute(str)

# Fetch a single row using fetchone() method.
db.commit()
# disconnect from server
db.close()
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Table Created</title>")
print ("</head>")
print ("<body>")
print ("<h2> Table is successfully created </h2>")
print ("</body>")
print ("</html>")

