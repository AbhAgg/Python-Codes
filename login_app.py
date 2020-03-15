import tkinter
from tkinter import *
import tkinter.messagebox
from sys import exit
import pymysql


def Welcome_Screen():
    if len (e1.get())==0 or len(e2.get()) == 0:
        Label(text='Both entries are necessary. ',justify="left",wraplength=100).grid(row=4,column=1)
        
    else:
        string="SELECT * from employee_details where name='"+e1.get()+"'and phone_number='"+e2.get()+"'"
        db = pymysql.connect("localhost","root","", database = "bank_database")
        cursor = db.cursor()
        cursor.execute(string)
        results = cursor.fetchall()
        db.commit()
        db.close()
        
        if results:
            for row in results:
                First_Name = row[0]
                Phone_Number = str(row[1])
        
            top = Toplevel()
            top.title("Hello New Window")
            top.geometry("300x200")
            lbl = Label(top,text="Hello "+e1.get()+", Welcome to python")
            lbl.grid(row=0,column=0)
            answerLabel.configure(text="")
    
        else:
            answerLabel.configure(text="No entry found, Please register")
            
        
        
def register_data(a,b,c):
    
    if len (a)==0 or len(b) == 0:
        Label(c,text='Both entries are necessary. ',justify="left",wraplength=100).grid(row=4,column=1)
    else:
        string="insert into employee_details values ('"+a+"','"+b+"') "

        db = pymysql.connect("localhost","root","", database = "bank_database")
        cursor = db.cursor()
        cursor.execute(string)
        db.commit()
        db.close()
        print("First Name: %s\nPhone Number: %s" % (a, b))
        Label(c,text='Your Entry has been added',justify="left",wraplength=100).grid(row=4,column=1)

    
def register():
    top = Toplevel()
    top.title("Enter Details Window")
    top.geometry("300x200")
    lbl = Label(top,text="Please Enter your details.")
    lbl.grid(row=0,column=0)
    
    Label1=Label(top, text = 'Username',justify="left")
    Label1.grid(row=1,column=0) 

    Label2=Label(top, text = 'Password',justify="left")
    Label2.grid(row=2,column=0)
    e3 = Entry(top) 
    e4 = Entry(top)
    e3.grid(row=1, column=1) 
    e4.grid(row=2, column=1)
    text1=e3.get()
    text2=e4.get()
    but1=Button(top,text="Register",command=lambda : register_data(e3.get(),e4.get(),top))
    but1.grid(row=3,column=1)
    

root = tkinter.Tk()
root.title ("Hello World")
root.geometry("300x200")


Label1=Label(root, text = 'Username',justify="left")
Label1.grid(row=0,column=1) 

Label2=Label(root, text = 'Password',justify="left")
Label2.grid(row=1,column=1)


e1 = Entry(root) 
e2 = Entry(root,text="")
e1.grid(row=0, column=2) 
e2.grid(row=1, column=2)


but1=Button(root,text="Register",command=register)
but1.grid(row=3,column=1)

but2=Button(root,text="Login",   command=Welcome_Screen)
but2.grid(row=3,column=2)
answerLabel = Label(root)
answerLabel.grid(row=4, column=1)

root.mainloop()