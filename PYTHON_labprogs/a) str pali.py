st=input("Input string : ")
rev=[]
for i in range(len(st)-1,-1,-1):
    rev.append(st[i])
rv="".join(rev)
print("Reversed string : ",rv)
if st!=rv:
    print("Not Pali")
else:
    print("Pali")