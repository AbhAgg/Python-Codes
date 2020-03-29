'''
class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
        
    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)
    
        
"This would create object of Employee class"
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print ("Total Employee %d" % Employee.empCount)

'''


'''

class Employee:

    
    def enter_details(self):
        self.EmployeeID = input("Enter the Employee ID: ")
        self.Name       = input('Enter the Name: ')
        self.Salary     = input('Enter the salary: ')
    
    
    def disp_details(self):
        print("Employee ID is: ", self.EmployeeID)
        print("Employee name is: ", self.Name)
        print("Employee salary is: ", self.Salary)
        

i=0
e=[]
for i in range(0, 3):
    
    emp=Employee()
    emp.enter_details()
    e.append(emp)


for i in range(0, 3):
    e[i].disp_details()

'''
'''
class Employee:
    
    def accept(self):
        self.EmployeeID = input("Enter the Employee ID: ")
        self.Name       = input('Enter the Name: ')
    
    def display(self):
        print("Employee ID is: ", self.EmployeeID)
        print("Employee name is: ", self.Name)
        
class temp_emp(Employee):
    def accept(self):
        Employee.accept(self)
        self.daily_wage=input('Enter Daily wage: ')
        print('\n')
        
    def display(self):
        Employee.display(self)
        print("Employee daily wage is: ", self.daily_wage)
        
class perm_emp(Employee):
    def accept(self):
        Employee.accept(self)
        self.house_rent=input('Enter House Rent: ')
        print('\n')
    def display(self):
        Employee.display(self)
        print("The house rent allowance is: ", self.house_rent)

p=[]
t=[]
while True: 
    print("1: Temporary Employee Data")
    print("2: Permanent Employee Data")
    print("3: Exit")
    a=int(input("Enter your Choice: \n"))
    
    if a==1:
            e=temp_emp()
            e.accept()
            t.append(e)
    
    elif a==2:
            emp=perm_emp()
            emp.accept()
            p.append(emp)
        
    elif a==3:
        print("Data of Temporary Employees")
        for k in range(0, len(i)):
            t[k].display()
        print("Data of Permanent Employees")    
        for k in range(0, len(j)):
            p[k].display()
        break
'''        

class Employee:

    def enter_details(self):
        self.EmployeeID = input("Enter the Employee ID: ")
        self.Name       = input('Enter the Name: ')
    
    def display_details(self):
        print("Employee ID is: ", self.EmployeeID)
        print("Employee name is: ", self.Name)
        
class temp_emp(Employee):
    def enter_daily_wage(self):
        Employee.enter_details(self)
        self.daily_wage=input('Enter Daily wage: ')
        print('\n')
        
    def disp_temp_data(self):
        Employee.display_details(self)
        print("Employee daily wage is: ", self.daily_wage)
        
class perm_emp(Employee):
    def house_rent(self):
        Employee.enter_details(self)
        self.house_rent=input('Enter House Rent: ')
        print('\n')
    def disp_perm_data(self):
        Employee.display_details(self)
        print("The house rent allowance is: ", self.house_rent)

e=[]   
f=[]     
while True: 
    print("1: Temporary Employee Data")
    print("2: Permanent Employee Data")
    print("3: Exit")
    a=int(input("Enter your Choice: \n"))
    
    if a==1:
        emp=temp_emp()
        emp.enter_daily_wage()
        e.append(emp)
        
    elif a==2:
        emp=perm_emp()
        emp.house_rent()
        f.append(emp)
            
    elif a==3:
        print("Data of Temporary Employees")
        for i in range(0, len(e)):
            e[i].disp_temp_data()
        print("Data of Permanent Employees")
        for j in range(0, len(f)):
            f[j].disp_perm_data()
        break