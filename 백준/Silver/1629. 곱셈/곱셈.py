import sys

a, b, c = map(int, sys.stdin.readline().split())


def Exp(a,b):
    if b == 1:
        return a
    k = Exp(a,b//2)%c
    if b % 2 == 0:
        return k*k
    else:
        return k*k*a


print(Exp(a,b)%c)