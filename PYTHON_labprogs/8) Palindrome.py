class Palstr:
    def __init__(self):
        self.ispali=False
    def pali(self,val):
        if val==val[::-1]:
            self.ispali=True
        return self.ispali

class Palint(Palstr):
    def __init__(self):
        super().__init__()
    def pali(self,val):
        temp=val
        rev=0
        while temp!=0:
            rev+=temp%10
            temp//=10
        if val==rev:
            self.ispali=True
        return self.ispali
o1=Palstr()
t=o1.pali(input("Enter a string : \n"))
if t:
    print("Palindrome")
else:
    print("Not Palindrome")
o2=Palint()
t=o1.pali(input("Enter an integer : \n"))
if t:
    print("Palindrome")
else:
    print("Not Palindrome")