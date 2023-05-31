import random


class Test:
    def __init__(self):
        self.x = None

    def intrandom(self, a, b, n):
        try:
            for _ in range(n):
                self.x = random.randint(a, b)
                print(_+1, ': The random integer generated is ', self.x)
        except Exception:
            print(a, 'is not less than ', b)


obj = Test()
try:
    p = int(input('Enter number of random integers to generate\n'))
    x, y = int(input('Enter the range: 2 numbers(both included)\n')), int(input())
    obj.intrandom(x, y, p)
except Exception:
    print('No valid data entered')
    exit()
