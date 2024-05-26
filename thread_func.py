from threading import Thread
from time import sleep


def f1():
    for i in range(1, 11):
        print(i, flush=True)
        sleep(1)


def f2():
    for i in range(ord('a'), ord('k')):
        print(chr(i), flush=True)
        sleep(1)


th_1 = Thread(target=f1)
th_2 = Thread(target=f2)

th_1.start()
th_2.start()

th_1.join()
th_2.join()
print('end')
