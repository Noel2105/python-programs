def F(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return F(n - 1) + F(n - 2)


num = int(input("Enter the number \n"))
if num > 0:
    print(num, "th Fibonacci number is", F(num))
    print("Fibonacci sequence of first",num,"terms is:")
    for i in range(1, num + 1):
        print(F(i), "\t", end="")
else:
    print("Enter a valid number")
