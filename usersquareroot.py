def sqroot(x):
    if x < 2:
        return x
    else:
        y = x
        z = (y + (x / y)) / 2

        while abs(y - z) >= 0.00000000000000000001:
            y = z
            z = (y + (x / y)) / 2
        return z


try:
    n = float(input('Enter a number'))
except:
    print('Didnt enter a number')
    exit()

print('Square root of ', n, 'is ', sqroot(n))
