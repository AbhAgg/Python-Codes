import _thread
import threading
import threaded
import time



class thread1:
    def __init__(self,a):
        
        for i in range (0,len(x)):
            threadLock.acquire()   
            print(x[i]+"\n")
            threadLock.release()
            time.sleep(1)
        
class thread2:
    def __init__(self,a):
        
        for i in range (0,len(y)):
            threadLock.acquire() 
            print(y[i]+"\n")
            threadLock.release()
            time.sleep(1)
       

        
try:
    x=list(input("Enter the First word:  "))
    y=list(input("Enter the Second word: "))
    threadLock = threading.Lock()
    t1=threading.Thread(target=thread1, args=(x,))
    t2=threading.Thread(target=thread2, args=(y,))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()

except:
    print("Unable to start thread.")    