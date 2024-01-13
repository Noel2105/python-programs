m1, m2, m3 = int(input("Enter 3 marks\n")), int(input()), int(input())
if m1 <= m2 and m1 <= m3:
    avg = (m2 + m3) / 2
elif m2 <= m1 and m2 <= m3:
    avg = (m1 + m3) / 2
else:
    avg = (m1 + m2) / 2
print("Average=", avg)
