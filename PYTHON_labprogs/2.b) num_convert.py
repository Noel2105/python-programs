def bin2dec(n):
    rev = n[::-1]
    dec = 0
    for i in range(len(n)):
        dec += int(rev[i]) * 2 ** i
    return dec


def oct2hex(n):
    rev = n[::-1]
    dec = 0
    for i in range(len(n)):
        dec += int(rev[i]) * 8 ** i
    l = []
    while dec != 0:
        l.append(str(dec % 16))
        dec = dec // 16
    nl = l[::-1]
    for i in range(len(nl)):
        if int(nl[i]) > 9:
            nl[i] = chr(ord('A') + int(nl[i]) - 10)
    hex = "".join(nl)
    return hex


bin = input("Enter binary number\n")
print("Decimal equivalent of", bin, "is", bin2dec(bin))
oct = input("Enter octal number\n")
print("Hexadecimal equivalent of", oct, "is", oct2hex(oct))
