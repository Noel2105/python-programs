sum = lambda x: (x * (x + 1)) / 2

try:
    n = int(input('Enter the number of natural numbers to add\n'))
    if n>0:
        print('Sum = ', sum(n))
    else:
        print('Enter a positive number')
except Exception:
    print('No valid number entered')
    exit()