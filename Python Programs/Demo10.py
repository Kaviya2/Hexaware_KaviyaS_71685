#Inheritance

class Emp:
    def __init__(self,firstname,age,salary,desig):
        self.firstname=firstname
        self.age=age
        self.salary=salary
        self.desig=desig
        
    def display(self):
        print("My Name is :",self.firstname,"Age :",self.age)
        
class Clerk(Emp):#inheriting Emp class
    def __init__(self,firstname,age,salary,desig):#without craeting own const, we use Emp class constrcu by inheriting
        Emp. __init__(self,firstname,age,salary,desig)#using Emp class constr
c=Clerk("Forcia",21,50000,"Clerk")
c.display()
