#%reset -f

'''
def factorial(a):
       fac=1
       for i in range (1,a+1):
        fac=fac*i       
       return fac;
a=int(input('Enter the Number: '))
f=factorial(a);
print('the factorial is: ',f)
'''

'''
def factorial(a):
    fac=1
    for i in range (1,a+1):
        fac=fac*i
    print('the factorial is' ,fac)
    return ;

a=int(input('Enter the Number'))
factorial(a);



def series(first,diff,last):
    s=0
    for i in range(first,last+1,diff):    
        s=s+i
        print(i,end='+')
    print("=",s)
first=int(input('enter the first value: '))
diff=int(input('enter the difference: '))
last=int(input('enter the last value: '))
result=series(first,diff,last)'''


'''

def series(first,diff,last):
    s=0
    for i in range(1,last+1):    
        s=s+first
        print(first,end='+')
        first=first+diff
        
    print("=",s)

first=int(input('enter the first value: '))
diff=int(input('enter the difference: '))
last=int(input('enter the last value: '))

result=series(first,diff,last)


'''


'''
def series(power,last):
    d=0
    for i in range(1,last+1):    
        s=i**power
        d=s+d
        if(i==last):
           print(s,end='')
        else:
           print(s,end='+')
    print("=",d)
power=int(input('enter the power: '))
last=int(input('enter the last value: '))

result=series(power,last)

'''

'''
    
    
def series(choice,last):
    
    if choice==1:
        t=0
        for i in range (2,int(last/2)+1):
            if last%i==0:
               print('Not a Prime Number') 
               t=1
               break
        if(t==0):
           print('Prime Number')
            
        
    if choice==2:
        s=0
        for i in range(0,last+1):
            s=s+i
            print(i,end='+')
        print('=',s)
        
        
r='y'
while (r=='y'):  
    choice=int(input('enter the series you want to print: '))
    last=int(input('enter the last value: '))
    series(choice,last)   
    r=input('Do you want to continue, y for yes, n for no')



'''



def series1(last):
    t=0
    for i in range (2,int(last/2)+1):
        if last%i==0:
           print('Not a Prime Number') 
           t=1
           break
    if(t==0):
       print('Prime Number')
         
           
           
def series2(last):
    s=0
    for i in range(0,last+1):
        s=s+i
        print(i,end='+')
    print('=',s)
                 
r='y'    
while r=='y':
    choice=int(input('enter the series you want to print: '))
    last=int(input('enter the last value: '))
    if choice==1:
        series1(last)
    if choice==2:
        series2(last)
    r=input('Do you want to continue, y for yes, n for no: ')

        
'''
def swap(a,b):
    return(b,a)

a=int(input('Enter the first Number (a): '))
b=int(input('Enter the second Number (b): '))
a,b=swap(a,b)
print('a=',a)
print('b=',b)
'''

'''

def total(a):
    y=sum(a)
    return y
r='y'
add=0
c=0
a=[]
while r=='y':
    q=int(input('Enter the math marks of the student: '))
    r=a.append(q)
    c=c+1
    print(a)
    r=input('Do you want to continue, y for yes, n for no: ')

s=input('Do you want to get the sum and percentage of all the numbers: ')
if s=='y':
    t=total(a)
    print('The sum of all the marks is: ',t)
    print('The percentage of all the marks is: ',t/c,'%')

'''
'''
def sec_hig(a):
    global p
    p=sorted(a.items(),key=lambda a:a[1],reverse=True)
    return (p[1],p)
r='y'
a={}
while r=='y':
    q=input('Enter the name of the student: ')
    v=int(input('Enter the marks of the student: '))
    a.update({q:v})
    print(a)
    r=input('Do you want to continue, y for yes, n for no: ')

    
s=input('Do you want to get the second highest number: ')
if s=='y':
    t,x=sec_hig(a)
    print(p)
    print('The second highest is:', t)
    

'''

import os
f0 = open("db.txt", "a")    
r='y'
p=[]
while r=='y':
    q=input('Enter the name of the student: ')+':'
    f0.write(q)
    v=input('Enter the marks of the student: ')
    f0.write(v+'\n')
    r=input('Do you want to continue, y for yes, n for no: ')
f0.close()

f0 = open("db.txt", "r")
f1 = open('temp.txt','w')
r=input('Enter the name you want to find: ')
line=f0.readline()
while  line:
    name,marks=line.split(":");
    if r==name:
        print(marks)
        marks = input('Enter the marks you want to replace of the student: ')
        print(marks)
        f1.write(name+':'+marks+'\n')
    else:
        f1.write(line)
    line=f0.readline()
    
f0.close()
f1.close()
os.remove('db.txt') 
os.rename('temp.txt', 'db.txt')
   
    
    
    
    
    
    
    
    