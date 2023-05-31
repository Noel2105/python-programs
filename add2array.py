from numpy import *

a = array([1, 2, 3, 4, 5])
b = array([6, 7, 8, 9, 10])
c = zeros([5])
for i in range(5):
    c[i] = a[i] + b[i]
print(c)
