import tkinter
from tkinter import *
import tkinter.messagebox
from sys import exit


root = tkinter.Tk()
root.title ("Hello World")
root.geometry("400x600")



def exitt():
    a=tkinter.messagebox.askokcancel(title="Example",message="Do you want to exit?")
    if a==True:
        root.destroy()

        
def sel():
    selection = "Value = " + str(var.get())
    label.config(text = selection)
var = DoubleVar()
scale = Scale( root, variable = var )
scale.pack(anchor=CENTER)

button = Button(root, text="Get Scale Value", command=sel)
button.pack(anchor=CENTER)



menu=Menu(root)
root.config(menu=menu)
subm=Menu(menu)
menu.add_cascade(label="File", menu=subm)
subm.add_command(label="Exit", command=exitt)




root.configure(bg="light blue")
but1=Button(root, padx=5,pady=5, text="Click", bg="powder blue", fg="green", font=("Times 20 bold"), command = exitt)
but1.pack()



#frame1=Frame(root,width=500,height=500,bg="green")
#frame1.pack()

labl1=Label(root,text="Name",font=("Times 20 bold"),width=4)
labl1.place(x=20,y=3)


text1=Text(root,width=10,height=10)
text1.place(x=200,y=300)


ent1=Entry(root ,font=("Times 20 bold"),width=4,cursor="dot",show="*")
ent1.place(x=200,y=100)


w=Checkbutton(root, bg="red",fg="black",cursor="dot",font=("Times 20 bold"),justify="left",selectcolor="yellow",state="normal",text="Hello World",height="10")
w.pack()


 
Lb = Listbox(root) 
Lb.insert(1, 'Python') 
Lb.insert(2, 'Java') 
Lb.insert(3, 'C++') 
Lb.insert(4, 'Any other') 
Lb.pack() 


menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit()) 

helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 


root.mainloop()
