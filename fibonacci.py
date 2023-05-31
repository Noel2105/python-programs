f0 = 0
f1 = 1
c = 0
n=int(input('Enter the number of fibonacci numbers to print\n'))
print(f0,'\t',end="")
print(f1,'\t',end="")
for i in range(n-2):
    fib = f0 + f1
    f0 = f1
    f1 = fib
    print(fib,'\t',end="")
    c += 1
print()
print(n,'fibonacci numbers printed')
