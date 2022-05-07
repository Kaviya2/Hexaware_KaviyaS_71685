#self as global variable
class Emp:
    def __init__(self,uid,name,age,salary,desig):
        self.uid=uid
        self.name=name
        self.age=age
        self.salary=salary
        self.desig=desig
        
    def display(self):
        print("Name: ",self.name)# global var - self
        print("ID: ",self.uid)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
        print("Designation: ",self.desig)
e=Emp(100,"Kaviya",21,50000,"CEO")#object creation
e.display()#calling method


#Same program but getting input from user
class Emp:
    def __init__(self):
        self.uid=input("Enter ID :")
        self.name=input("Enter Name :")
        self.age=int(input("Enter Age :"))
        self.salary=int(input("Enter Salary:"))
        self.desig=input("Enter Designation :")
        
    def display(self):
        print("Name: ",self.name)# global var - self
        print("ID: ",self.uid)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
        print("Designation: ",self.desig)
e=Emp()#creating obj
e.display()#calling method
