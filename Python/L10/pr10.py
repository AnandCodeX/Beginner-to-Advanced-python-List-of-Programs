#wapp for multi threading OOP
import threading
import time
class writing(threading.Thread):
    def run(self):
        print("writting assg.")
        for i in range(1,11):
            print('writing',i,'assignment')
            time.sleep(0.5)
        print("writting completed")
class music(threading.Thread):
    def run(self):
        print("writting assg.")
        for i in range(1,20):
            print('music',i,'running')
            time.sleep(0.5)
        print("music stoped")

print("ajj ka kam shuru")
w=writing()
m=music()
w.start()
m.start()
w.join()
m.join()
print("aaj ka kam khtam")