#race condition threading solution

import threading
import time

balance=500
s=threading.Semaphore()

def deposite():
    print("dep. process start")
    s.acquire()
    global balance
    amt1=balance+100
    time.sleep(2)
    balance=amt1
    s.release()
    print("dep process ended")

def withdrow():
    print("with. process start")
    s.acquire()
    global balance
    amt2=balance-100
    time.sleep(2)
    balance=amt2
    s.release()
    print("dep process ended")

print("initial bal =",balance)
t1=threading.Thread(target=deposite)
t2=threading.Thread(target=withdrow)
t1.start()
t2.start()
t1.join()
t2.join()
print("final bal =",balance)