#race conditionj threading

import threading
import time

balance=500

def deposite():
    print("dep. process start")
    global balance
    amt1=balance+100
    time.sleep(2)
    balance=amt1
    print("dep process ended")

def withdrow():
    print("with. process start")
    global balance
    amt2=balance+-100
    time.sleep(2)
    balance=amt2
    print("dep process ended")

print("initial bal =",balance)
t1=threading.Thread(target=deposite)
t2=threading.Thread(target=withdrow)
t1.start()
t2.start()
t1.join()
t2.join()
print("final bal =",balance)