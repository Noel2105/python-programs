import array as arr

a = arr.array('i', [])
n = int(input('Enter size of array\n'))
print('Enter all the elements\n')
for i in range(n):
    x = int(input())
    a.append(x)
print(a)

print()
c = 0
k = int(input('Enter key element to be searched'))
for i in a:
    if k == i:
        print(c)
        break
    c += 1
else:
    print('Key not found') 
try:
    print(a.index(k))
except Exception as E:
    print(E)

