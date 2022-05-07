def abc():#function
    for i in range(10):
        print("Function: " ,i)
abc()#calling func

class Demo:
    def __init__(self): # constructor
        for i in range(10):
            print("Constructor: ",i)
    def display(self): # method
        for i in range(10):
            print("Method :",i)
d=Demo()
d.display()

print("================Parameterized Constructor and Method==============")
class Demo:
    def __init__(self,uid,name,age): # parameterized constructor
        for i in range(10):
            print("Constructor: ",uid,name,age)
    def display(self,salary,desig): # parameterized method
        for i in range(10):
            print("Method :",i,salary,desig)
d=Demo(100,"Kaviya",21)
d.display(50000,"Manager")
