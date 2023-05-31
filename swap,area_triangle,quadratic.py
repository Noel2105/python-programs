from cmath import *


def swap(x, y):
    x, y = y, x
    return x, y


def area_bh(base, height):
    area = 1 / 2 * base * height
    return area


def area_sides(x, y, z):
    s = (x + y + z) / 3
    ar = sqrt(s * ((s - x) + (s - y) + (s - z)))
    return ar


def quadratic(a, b, c):
    r1, r2 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a), (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
    return r1, r2


m, n = int(input('Enter 1st number to swap\n')), int(input('Enter the 2nd number\n'))
m, n = swap(m, n)
print('The new values of a and b are:\n', m, n)

ch = int(input('Area of triangle:\n1-->Base and height\n2-->All the sides\n'))
if ch == 1:
    b, h = float(input('Enter base and height\n')), float(input())
    print('Area:', area_bh(b, h))
elif ch == 2:
    a, b, c = float(input('Enter all the 3 sides\n')), float(input()), float(input())
    print('Area:', area_sides(a, b, c))
else:
    print('No valid choice!!')

p, q, r = float(input('Enter 3 co-efficients of quadratic equation\n')), float(input()), float(input())
s, t = quadratic(p, q, r)
print('Roots are :\nRoot 1 = ', s,'\nRoot 2 = ', t)
