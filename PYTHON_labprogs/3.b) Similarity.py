s1=input("Enter first string")
s2=input("Enter second string")
if len(s1)>len(s2):
    long=s1
    short=s2
else:
    long = s2
    short = s1
mc=0
for i in range(len(short)):
    if s1[i]==s2[i]:
        mc+=1
sim=mc/len(long)
print("Similarity is",sim)