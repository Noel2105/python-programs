miles = lambda km: km / 1.6093
kms = lambda m: m * 1.6093
farenheit = lambda celsius: (celsius * (9 / 5)) + 32
cels = lambda frnht: (frnht - 32) * (5 / 9)

while 1:
    try:
        n = int(input('\nEnter choice\n1->Kms to miles\n2->Miles to kms\n3->Celsius to fahrenheit\n4->Fahrenheit to '
                      'celsius\n5->Exit\n'))
        if n == 1:
            print('Miles ', miles(float(input('Enter km\n'))),'\n')
        elif n == 2:
            print('Kilometers ', kms(float(input('Enter miles\n'))),'\n')
        elif n == 3:
            print('Fahrenheit ', farenheit(float(input('Enter the temperature in celsius\n'))),'\n')
        elif n == 4:
            print('Celsius ', cels(float(input('Enter the temperature in farenheit\n'))),'\n')
        elif n == 5:
            exit()
        else:
            print('Enter a valid choice\n')
    except Exception:
        print('No number entered')
