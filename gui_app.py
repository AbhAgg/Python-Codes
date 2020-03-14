import tkinter
from tkinter import *
import tkinter.messagebox
from sys import exit
import pymysql

#cursor = db.cursor()

def enter_data():
    string="insert into employee_details values ('"+e1.get()+"','"+e2.get()+"')"

    db = pymysql.connect("localhost","root","", database = "bank_database")
    cursor = db.cursor()
    cursor.execute(string)
    db.commit()
    db.close()
    print("First Name: %s\nPhone Number: %s" % (e1.get(), e2.get()))
    Label(root, text='Your Entry has been added',justify="left",wraplength=100).grid(row=4,column=1)

    
def search_data():
    global myLabel
    string="SELECT * from employee_details where name='"+e1.get()+"'"
   
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
        
        
        x=("First_Name: %s \n Phone_Number: %s" % (First_Name,Phone_Number))
        answerLabel.configure(text=x)
        e2.delete(0,END)
        e2.insert(0,Phone_Number)
    else:
        answerLabel.configure(text="No entry found, Please register")
        e2.delete(0,END)
        e2.insert(0,"No Entry Found")
    
def delete_data():
    string="delete from employee_details where name='"+e1.get()+"'"
    db = pymysql.connect("localhost","root","", database = "bank_database")
    cursor = db.cursor()
    cursor.execute(string)
    db.commit()
    db.close()   

    Label(root, text='Your entry has been deleted',wraplength=100).grid(row=4,column=1)


def edit_data():
    string="update employee_details set name='"+e1.get()+"', phone_number='"+e2.get()+"' where name='"+e1.get()+"'"
    db = pymysql.connect("localhost","root","", database = "bank_database")
    cursor = db.cursor()
    cursor.execute(string)
    db.commit()
    db.close() 
    Label(root, text='Your entry has been edited',wraplength=100).grid(row=4,column=1)


 
root = tkinter.Tk()
root.title ("Hello World")
root.geometry("300x300")


#txt = Entry(root,font=("Times 20 bold"),width=10)
#txt.grid(column=1, row=0)

Label1=Label(root, text = 'First Name',  justify="left")
Label2=Label(root, text = 'Phone number',justify="left")
Label1.grid(row=0,column=1) 
Label2.grid(row=1,column=1)


e1 = Entry(root) 
e2 = Entry(root,text="")
e1.grid(row=0, column=2) 
e2.grid(row=1, column=2)


but1=Button(root,text="Add Entry",command=enter_data)
but1.grid(row=3,column=1)

but2=Button(root,text="Search",   command=search_data)
but2.grid(row=3,column=2)

but3=Button(root,text="Delete",   command=delete_data)
but3.grid(row=3,column=3)

but4=Button(root,text="Edit",     command=edit_data)
but4.grid(row=3,column=4)

answerLabel = Label(root)
answerLabel.grid(row=4, column=1)

root.mainloop()