# builtin function using numpy

from numpy import *

print('LCM is :', lcm(int(input('Enter 2 numbers\n')), int(input())))

# from user defined function

p = 0


def lcmnum(m, n):
    globals()['p'] += n
    if p % m == 0 and p % n == 0:
        pass
    else:
        lcmnum(m, n)


x, y = int(input('Enter 2 numbers to find LCM\n')), int(input())
if x < y:
    lcmnum(x, y)
else:
    lcmnum(y, x)
print('LCM is :', p)
