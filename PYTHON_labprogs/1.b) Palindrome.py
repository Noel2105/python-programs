st=input("Enter the value\n")
set=[]
rev=st[::-1]
if st==rev:
    print("Palindrome")
else:
    print("Not palindrome")
for i in range(len(st)):
    if st[i] not in set:
        print(st[i],"appears",st.count(st[i]),"times")
        set.append(st[i])