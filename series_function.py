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

















































