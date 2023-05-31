try:
    n, d = int(input('Enter 2 numbers to check divisibility\n')), int(input())
    if n % d == 0:
        print(n, 'is divisible by ', d)
    else:
        print(n, 'is not divisible by ', d)
except Exception:
    print('No valid integer entered')
