try:
    y = int(input('Enter the year to check\n'))
    if y<0:
        print("Year can't be negative")
        exit()
except Exception:
    print('No valid integer entered')
    exit()
if y % 4 == 0:
    print(y, 'is a leap year')
else:
    print(y, 'is not a leap year')
