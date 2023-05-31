


def displ(list):
    print()
    for i in list:
        if len(i) <= 5:
            print(i)


l = []

print('Enter 10 names')
for i in range(10):
    l.append(input())

displ(l)
