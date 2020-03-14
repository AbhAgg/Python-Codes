import _thread
import threading
import threaded
import time


class thread1:
    def __init__(self,a):
        self.number = a 
        for i in range(0,11):
            print(i+self.number)
        
        
class thread2:
    def __init__(self,a):
        self.number = a 
        for i in range(0,11):
            print(i+self.number)    
        
        
        
        
try:
    i=0
    while i<6:
        
        t1=threading.Thread(target=thread1, args=(10+i*10,))
        t2=threading.Thread(target=thread2, args=(400+i*10,))
    
        t1.start()
        t1.join()
        t2.start()
        t2.join()
        i=i+1
except:
    print ("Error: unable to start thread")