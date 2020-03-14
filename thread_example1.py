import _thread
import threading
import threaded
import time
# Define a function for the thread

class print_thread:
    
    
    def thread1(a):
        if a==20:
            for i in range(0,a+1):
                print(i)
                #time.sleep(0.1)
    
        if a==40:
            for i in range(21,a+1):
                print(i)
                #time.sleep(0.1)       
# Create two threads as follows
try:
    t1=threading.Thread(target=print_thread.thread1, args=(20,))
    t2=threading.Thread(target=print_thread.thread1, args=(40,))
    
    
    t1.start()
    t2.start()
    
    print("---------------")
    
    #_thread.start_new_thread( print_thread.thread1, (20,))
    #_thread.start_new_thread( print_thread.thread1, (40,))
    
    #print("Hello World T1",t1.isAlive())
   # print("Hello World T2",t2.isAlive())
    
    t1.join()
    t2.join()
    print("Hello World T1",t1.isAlive())
    print("Hello World T2",t2.isAlive())
    for i in range(91,100):
                print(str(i)+'a')
    

except:
    print ("Error: unable to start thread")
    