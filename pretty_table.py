

#%reset -f
d={}
from tabulate import tabulate
from prettytable import PrettyTable
    
table = PrettyTable()
table.field_names = ["Roll Number", "Name", "Math Marks", "Hindi Marks","Punjabi Marks",'Total Marks','percentage']
Total_Marks=0


x='y'
while x=='y':
      rollnum=input("Enter the roll number  of the student: ")
      name=input('Enter the name of the student: ')
      math=input('Enter math marks of the student: ')
      hindi=input('Enter hindi marks of the student: ')
      punjabi=input('Enter punjabi marks of the student: ')
      d[rollnum]=[name,math,hindi,punjabi]
      print(d)
      x=input('Do you want to make another entry(y/n) : ')
print()
rollnum=0
q1=list(d.keys())
q2=list(d.values())
name1,math1,hindi1,punjabi1,marks,percentage=[],[],[],[],[],[] 
roll_num=list(d.keys())
for i in range(0,len(d)):
    name1.append(q2[i][0])
    math1.append(q2[i][1])
    hindi1.append(q2[i][2])
    punjabi1.append(q2[i][3])
    
for i in range(0,len(q2)):
    Total_Marks=0
    for j in range(1, 4):
        Total_Marks=int(q2[i][j])+Total_Marks
        
    marks.append(Total_Marks)
    percentage.append("{0:.2f}".format((Total_Marks/300)*100))
    d[str(i+1)]=[name,math,hindi,punjabi,marks[i],percentage[i]]

        
        
for i in range (0,len(roll_num)):
    table.add_row([roll_num[i],name1[i],math1[i],hindi1[i],punjabi1[i],marks[i],percentage[i]])
print(table)



'''

d={1:['sam',456], 2:['rham',123]}

for key, value in sorted(d.items(),key=lambda a:a[1][1]):
    print (key,value)
    
'''