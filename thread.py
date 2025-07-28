import threading

counter = 0
lock =  threading.Lock()

#create def1
def thread1():
    global counter
    for i in range(100000):
        with lock:
            counter += 1
        
#create def2
def thread2(): 
    global counter
    for i in range(100000):
        with lock:
            counter -= 1
           
#create the two threads
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

#start thethreads
t1.start()
t2.start()

#wait for the threads to finish 
t1.join()
t2.join()

#print the final value of the counter
print("Counter:", counter)