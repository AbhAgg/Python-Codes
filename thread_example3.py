import _thread
import threading
import threaded
import time


class thread1:
    def __init__(self,a):
        self.number = a 
        for i in range(1,50):
            print(i+self.number)
            if i%10==0:
                time.sleep(1)
   
class thread2:
    def __init__(self,a):
        self.number = a 
        for i in range(51,101):
            print(i+self.number)
            if i%10==0:
                time.sleep(1)
             
try:       
        t1=threading.Thread(target=thread1, args=(10,))
        t2=threading.Thread(target=thread2, args=(400,))
    
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    
except:
    print ("Error: unable to start thread")