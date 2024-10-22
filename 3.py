import threading
import time

def square(n):
    print(n*n)
    
l = [1,2,3,4,5,6,7,8,9]
for i in l:
    t = threading.Thread(target = square, args = (i,))
    t.start()
    time.sleep(1)
