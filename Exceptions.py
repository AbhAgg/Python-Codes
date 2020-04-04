'''try:
        a=int(input('Enter the number: '))
        b=int(input('Enter the number: '))
        c=a/b
        print("Result = ",c)       
except :   
        print('Enter the number greater than zero')
        '''
        
'''  
a=[]        
i=0
while True:
    try:
        a.append(int(input('Please enter {0} number: '.format(i+1))))
       
        if (type(a[i])==str):
           raise ValueError
        i=i+1
    except ValueError:
        print("Oops!  That was a character. Please enter a number...")
        break
'''
'''
a=[]
i=1
while True:
    if i<6:
        try:
            a.append(int(input('Please enter the {0} marks: '.format(i))))
            if a[i-1]>0 and a[i-1]<100:
                print(a[i-1])
                i=i+1
        except ValueError:
            print("Oops! That was a character. Please enter a number...")
            a.append(0)
    else:
        break
    '''

i=1
while i<6:
    try:
        a=int(input('Please enter the {0} marks: '.format(i)))
        if a>0 and a<100:         
            print(a)
            i=i+1
        else:
            raise ValueError
    except ValueError:
        print("Oops! That was a character. Please enter a number...")
