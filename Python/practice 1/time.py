
from time import time

def func1(a,b):
    # rohan das
    return a+b

def func2(a,b):
    # Hemant
    num1=a
    num2=b
    if (a>b and a!=3):
        pass
    sum([a,b])
    return a+b

if __name__ == '__main__':
    init=time()
    for i in range (0,1000000):
            func1(3,5)
    print("Rohan das time: ", time()-init)
    init=time()
    for i in range (0,1000000):
            func2(3,5)
    print("Hemant time: ", time()-init)

print("overall time", time()-init)
