def armstrng(n, l):
    sum = 0
    for i in range(l):
        try:
            sum += pow(int(n[i]), l)
        except Exception:
            print('No positive number entered')
            exit()
    if sum == int(n):
        print(int(n), 'is an armstrong number')
    else:
        print(int(n), 'is not an armstrong number')


x = input('Enter a number\n')
ln = len(x)
armstrng(x, ln)
