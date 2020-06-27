#wapp for multi threading POP
import threading
import time
def writing():
    print("writting assg.")
    for i in range(1,11):
        print('writing',i,'assignment')
        time.sleep(0.5)
    print("writting completed")

def music():
    print("writting assg.")
    for i in range(1,20):
        print('music',i,'running')
        time.sleep(0.5)
    print("music stoped")

print("ajj ka kam shuru")
w=threading.Thread(target=writing)
m=threading.Thread(target=music)
w.start()
m.start()
w.join()
m.join()
print("aaj ka kam khtam")