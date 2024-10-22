import threading
import time

def sec():
    for i in range(1,10):
        print(i)
        time.sleep(1)

t1 = threading.Thread(target = sec)
t1.start()
t2 = threading.Thread(target = sec)
t2.start()