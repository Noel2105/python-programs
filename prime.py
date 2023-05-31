c = 0
x = int(input('Enter an integer\n'))
if x == 0 or x == 1:
    print('Neither prime nor composite')
else:
    for i in range(2, int(x / 2) + 1):
        if x % i == 0:
            c = 1
            break
    if c == 0:
        print(x, 'is prime')
    else:
        print(x, 'is not prime')
