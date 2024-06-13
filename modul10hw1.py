import time
from threading import Thread


def qwerty(inter):
    for i in range(inter):
        print(i)
        time.sleep(1)


def ytrewq(stroki):
    for element in range(0, len(stroki)):
        print(stroki[element])
        time.sleep(1)


thread = Thread(target=qwerty, kwargs=dict(inter=11))
thread.start()

ytrewq(stroki='abcdefghij')

thread.join()
