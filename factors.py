n= int(input('Enter a number\n'))
print('Factors are :\n0')
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
