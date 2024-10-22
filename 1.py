import threading

def square():
    for i in range(1,10):
        print( "квадрат числа ", i ," = ", i*i)

def cube():
    for i in range(1,10):
        print( "куб числа " , i ," = ", i*i*i)        

t1 = threading.Thread(target = square)
t1.start()
t2 = threading.Thread(target = cube)
t2.start()