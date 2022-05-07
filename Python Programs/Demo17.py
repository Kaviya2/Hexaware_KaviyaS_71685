class Student:
    def __init__(self,name,age,salary):
        self.age=age#public
        self._name=name#protected
        self.__salary=salary#private

    def display(self):
        print("Age :",self.age)
        print("Name :",self._name)
        print("Salary :",self.__salary)

s=Student("Kaviya",25,40000)
s.display()

print(s.age)
print(s._name)
#print(s.__salary) - not allowed bcoz it is private
