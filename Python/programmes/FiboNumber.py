# Fibonumber
import time


def fiboIter(n):
    prevnum = 0
    currentnum = 1
    for i in range(1, n):
        prevprevnum = prevnum
        prevnum = currentnum
        currentnum = prevprevnum + prevnum
    return currentnum


def fiboRecur(n):
    if n == 0 or n == 1:
        return n
    else:
        return fiboRecur(n-1)+fiboRecur(n-2)


if __name__ == "__main__":
    num = int(input("Enter the number: "))
    _init_ = time.time()
    print(f"using iter value of fib({num}) is {fiboIter(num)}")
    print(f"It took {time.time() - _init_} seconds")
    print(f"using Recursion value of fib({num}) is {fiboRecur(num)}")
    print(f"It took {time.time() - _init_} seconds")
