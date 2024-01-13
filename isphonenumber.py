import re


def isphonenumber(num):
    if len(num) != 12:
        return False
    for i in range(len(num)):
        if i == 3 or i == 7:
            if num[i] != '-':
                return False
        elif num[i].isdigit() == False:
            return False
    return True


def checkphone(num):
    phnumpattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    if phnumpattern.match(num):
        return True
    else:
        return False


ph_num = input("Enter a phone number:\n")
print("Without using regular expression:\n")
if isphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")

print("Using regular expression:")
if checkphone(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")
