strval = input("Enter a value :\n")
if strval == strval[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
for i in range(len(strval)):
    if strval.count(strval[i]) > 0:
        print(strval[i], "appears", strval.count(strval[i]), "times")
