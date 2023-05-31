str1 = "ABCD"
str2 = "PQR"
i = 0
while i < len(str1):
    for j in range(0, i + 1):
        print(str1[j], end=" ")
    for k in range(i, len(str2)):
        print(str2[k], end=" ")
    i += 1
    print()
