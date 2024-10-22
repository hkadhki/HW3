from multiprocessing import Process, Pipe

def factorial(n):
    res = 1
    for i in range(1,n + 1):
        res = res * i
    print("факториал числа ", n ," = ", res)

if __name__ == "__main__":
    n = 10
    for i in range(1,n + 1):
        Process(target=factorial, args=(i,)).start()