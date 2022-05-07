#Global Variable Usage

class Clerk:
    salary=15000#global var
    desig="CLERK"#global var
    
    def __init__(self):#constructor
        self.uid=input("Enter ID :")
        self.name=input("Enter Name :")
        self.age=int(input("Enter Age :"))
    
    def display(self):#method
        print("Employee Details...")
        print("Name: ",self.name)# global var - self
        print("ID: ",self.uid)
        print("Age: ",self.age)
        print("Salary: ",self.salary)#salary is global var
        print("Designation: ",self.desig)#desig is global var
        
    def raiseSal(self):
        print("After Raising the salary...")
        print("Name: ",self.name)# global var - self
        print("ID: ",self.uid)
        print("Age: ",self.age)
        print("Salary: ",self.salary+20000)#even we declared salary in the above, have to use self
        print("Designation: ",self.desig)

            
e=Clerk()#creating obj
e.display()#calling method
e.raiseSal()#calling method
