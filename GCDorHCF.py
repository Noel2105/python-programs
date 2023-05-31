# builtin function in numpy

from numpy import *

print('GCD is :',gcd(int(input('Enter 2 numbers\n')), int(input())))


# user defined function

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


x, y = int(input('Enter 2 numbers\n')), int(input())
print('GCD is :', gcd(x, y))
