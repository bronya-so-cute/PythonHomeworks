import string
import random

set1 = set()

def getdata():
    for i in range(1000):
        a = random.uniform(0, 100)
        set1.add(a)
    for i in range(1000):
        a = (''.join(random.sample(
            ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
             'e', 'd', 'c', 'b', 'a'], 4)))
        set1.add(a)

def choose():
    for i in set1:
        if (type(i) == type(1.2)):
            if (i >= 20 and i <= 50):
                print(i)
        if (type(i) == type('str')):
            if ('at' in i):
                print(i)

def mainfun():
    if __name__ == '__main__':
        getdata()
        choose()
