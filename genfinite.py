from llist import Node, LList, append
from math import gcd

def finite(n):
    lst = LList()
    f = lambda x: (x*x+1) % n
    x = y = 2
    d = 1
    while d == 1:
        append(lst, Node(x))
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x-y), n)
    return lst

lst = finite(99990001)
