def fib(x, c=0):
    global f0, f1
    if c == 0:
        f0 = 0
        f1 = 1
        print(f0, '\t', end="")
        print(f1, '\t', end="")
    if c != x - 2:
        f2 = f0 + f1
        print(f2, '\t', end="")
        f0 = f1
        f1 = f2
        c += 1
        return fib(x, c)
    else:
        pass


n = int(input('Enter number of fibonacci numbers\n'))
fib(n)
