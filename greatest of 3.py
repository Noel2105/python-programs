print('Enter 3 numbers')
a = float(input())
b = float(input())
c = float(input())
if a > b and a > c:
    print(a, ' is greatest')
elif b > a and b > c:
    print(b, ' is greatest')
else:
    print(c, ' is greatest')
