def prm(x, y):
    if y<x:
        print('NULL')
        return
    for i in range(x, y + 1):
        c = 0
        if i == 0 or i == 1:
            print(i, 'is neither prime nor composite')
        else:
            for j in range(2, int((i / 2)+1)):
                if i % j == 0:
                    c = 1
            if c == 0:
                print(i)

try:
    a, b = int(input('Enter 2 integers as range\n')), int(input())
    if a<0 or b<0:
        print('Enter a positive range')
        exit()
except Exception:
    print('No valid integers entered')
    exit()
print('The prime numbers in the range [', a, ',', b, '] are :\n')
prm(a, b)
