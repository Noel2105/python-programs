import re


def woregex(str):
    if len(str) != 12:
        return False
    for i in range(len(str)):
        if i == 3 or i == 7:
            if str[i] != '-':
                return False
        else:
            if not str[i].isdigit():
                return False
    return True


pat = re.compile(r'^\d{3}-\d{3}-\d{4}$')


def withregex(str):
    if globals()['pat'].match(str):
        return True
    else:
        return False


st = input("Enter a string")
if woregex(st):
    print("Without regex : MATCHED")
else:
    print("Without regex : NOT MATCHED")
if pat.match(st):
    print("With regex : MATCHED")
else:
    print("With regex : NOT MATCHED")
