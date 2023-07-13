m1 = int(input("Enter marks for test 1 : \n"))
m2 = int(input("Enter marks for test 2 : \n"))
m3 = int(input("Enter marks for test 3 : \n"))

avg = 0.0
if m1 <= m2 and m1 <= m3:
    avg = (m2 + m3) / 2
elif m2 <= m1 and m2 <= m3:
    avg = (m1 + m3) / 2
elif m3 <= m1 and m3 <= m2:
    avg = (m1 + m2) / 2
print("The average of best two test marks out of three test is : ", avg)
