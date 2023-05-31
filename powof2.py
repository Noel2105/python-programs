try:
    n = float(input('Enter the power for 2\n'))
except Exception:
    print('INVALID DATA')
    exit()
print(2 ** n)
