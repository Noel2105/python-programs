from numpy import *

n = int(input('Enter the size of the array'))
a = zeros([n], int)
print('Enter all the elements')
for i in range(n):
    a[i] = int(input())
print('Your array is ', a)
temp = a[0]
for i in range(1, n):
    if a[i] > temp:
        temp = a[i]
print('Largest is ', temp)
