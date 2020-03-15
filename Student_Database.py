#!C:\Users\abhin\AppData\Local\Programs\Python\Python38-32/python

import pymysql
import cgi,cgitb
import os
form = cgi.FieldStorage()
flag=0
Roll_Num       = form.getvalue('Roll_Num')
Student_Name   = form.getvalue('Student_Name')
Class          = form.getvalue('Class')
Math_Marks     = form.getvalue('Math_Marks')
English_Marks  = form.getvalue('English_Marks')
Punjabi_Marks  = form.getvalue('Punjabi_Marks')
Hindi_Marks    = form.getvalue('Hindi_Marks')
db = pymysql.connect("localhost","root","", database = "student_database")
cursor = db.cursor()


if form.getvalue("SUBMIT"):
    str="insert into class_data values ( " +Roll_Num+",'" +Student_Name+"'," +Class+",\
    " +Math_Marks+",\
    " +English_Marks+",\
    " +Punjabi_Marks+",\
    " +Hindi_Marks+")"
    cursor.execute(str)
    flag=1
if form.getvalue("DELETE"):
    str="delete from class_data where Roll_Num = " +Roll_Num+""
    cursor.execute(str)
    flag=2

if form.getvalue("EDIT"):
    str="update class_data set Name='"+Student_Name+"',\
        Class=" +Class+",\
        Math_Marks=" +Math_Marks+",\
        English_marks=" +English_Marks+",\
        Punjabi_Marks=" +Punjabi_Marks+",\
        Hindi_Marks=" +Hindi_Marks+"\
        where Roll_Num=" +Roll_Num+""
    cursor.execute(str)
    flag=3
    
if form.getvalue("SEARCH"):
    str="SELECT * FROM class_data WHERE Roll_Num =" +Roll_Num+""
    cursor.execute(str)
    results = cursor.fetchall()
    for row in results:
        Student_Name = row[1]
        Class = row[2]
        Math_Marks = row[3]
        English_Marks = row[4]
        Punjabi_Marks = row[5]
        Hindi_Marks   = row[6] 
        
    flag=4


db.commit()
db.close()

if flag==1:
    print ("Content-type:text/html\r\n\r\n")
    print ("<html>")
    print ("<head>")
    print ("<title>Table Created</title>")
    print ("</head>")
    print ("<body>")
    print ("<h2> Entry is successfully added </h2>")
    print ("</body>")
    print ("</html>")

if flag==2:
    print ("Content-type:text/html\r\n\r\n")
    print ("<html>")
    print ("<head>")
    print ("<title>Table Created</title>")
    print ("</head>")
    print ("<body>")
    print ("<h2> Entry is successfully deleted </h2>")
    print ("</body>")
    print ("</html>")
    
    
if flag==3:
    print ("Content-type:text/html\r\n\r\n")
    print ("<html>")
    print ("<head>")
    print ("<title>Table Created</title>")
    print ("</head>")
    print ("<body>")
    print ("<h2> Entry is successfully edited </h2>")
    print ("</body>")
    print ("</html>")
        
if flag==4:
    print ("Content-type:text/html\r\n\r\n")
    
    '''
    print ("<html>")
    print ("<head>")
    print ("<title>Table Created</title>")
    print ("</head>")
    print ("<body>")
    print ("<p> The Name is: %s</p>" %(Student_Name))
    print ("<p> Class is: %s</p>" %(Class))
    print ("<p> Math Marks: %s</p>" %(Math_Marks))
    print ("<p> English Marks: %s</p>" %(English_Marks))
    print ("<p> Punjabi Marks: %s</p>" %(Punjabi_Marks))
    print ("<p> Hindi Marks: %s</p>" %(Hindi_Marks))
    print ("</body>")
    print ("</html>")
    '''
      
    print("<html>")
    print("<head>")
    print("<title>")
    print("Student Database")
    print("</title>")
    print("</head>")
    print("<body>")
    print("<table border='1' width='400px'>")
    print("<tr> <th colspan='12' align='Center'>Student Database </th></tr>")
    print("<tr> <td colspan='6'>Enter Roll Number</td>")
    print("<td colspan='6'> <input type='number' name='Roll_Num'       placeholder='%s'   maxlength='15'></td></tr>"%Roll_Num)
    
    print("<tr> <td colspan='6'>Enter Student Name</td>")
    print("<p><td colspan='6'>  %s</p></td></tr>" %(Student_Name))
    
    print("<tr> <td colspan='6'>Enter Class</td>")
    print("<td colspan='6'> <input type='text'   name='Class'          value='%s'  maxlength='15' pattern='[a-zA-Z0-9]*'></td></tr>" %(Class))
    print("<tr> <td colspan='6'>Math Marks</td>")
    print("<td colspan='6'> <input type='number' name='Math_Marks'     placeholder='%s'     maxlength='15' ></td></tr>"%(Math_Marks))
    print("<tr> <td colspan='6'>English Marks</td>")
    print("<td colspan='6'> <input type='number' name='English_Marks'  placeholder='%s'     maxlength='15' ></td></tr>"%(English_Marks))
    print("<tr> <td colspan='6'>Punjabi Marks</td>")
    print("<td colspan='6'> <input type='number' name='Punjabi_Marks'  placeholder='%s'     maxlength='15' ></td></tr>"%(Punjabi_Marks))
    print("<tr> <td colspan='6'>Hindi Marks</td>")
    print("<td colspan='6'> <input type='number' name='Hindi_Marks'    placeholder='%s'     maxlength='15' ></td></tr>"%(Hindi_Marks))
    
    print("<tr>  <td colspan='3'><input type='submit' value='SUBMIT' name='SUBMIT'>")
    print("      <td colspan='3'><input type='submit' value='DELETE' name='DELETE'>")
    print("      <td colspan='3'><input type='submit' value='EDIT'   name='EDIT'>")
    print("      <td colspan='3'><input type='submit' value='SEARCH' name='SEARCH'> </td>")
    
    
    print("</form>")
    print("</body>")
    print("</table>")
    print("</html>")
        
        
    