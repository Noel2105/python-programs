class Employee:
    def __init__(self):
        print("Enter employee details")
        self.name=input("Name : ")
        self.empid=input("ID : ")
        self.dept=input("Department : ")
        self.sal=int(input("Salary : "))
    def show(self):
        print("Employee details are :")
        print("NAME : ",self.name,"\nID : ",self.empid,"\nDEPT : ",self.dept,"\nSALARY : ",self.sal)
    def update(self):
        print("Enter the new salray : ")
        self.sal=int(input())
        print("The updated salary is : ",self.sal)

o=Employee()
o.show()
o.update()