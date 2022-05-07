#Inheritance

class Cal:
    def addition(self,a,b):
        print(a+b)
class MyCal:
    def subtraction(self,a,b):
        print(b-a)

class Cal2(Cal,MyCal):#inheriting class 1 & class 2 
    def multi(self,a,b):
        print(a*b)

c2=Cal2()
c2.addition(100,600)
c2.multi(10,20)
c2.subtraction(200,100)
    
