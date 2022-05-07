class P:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def display(self):
        print("My frist name is : ",self.firstname,"last name is: ",self.lastname)

class C(P):#inheritance
    def __init__(self,firstname,lastname):
        P.__init__(self,firstname,lastname)#callling P class constructor

#p=P("Kaviya","Aishwarya")# if we non comment this, it will be printed else that one
#p.display()

c=C("Elakkiya","Saranya")#passing values for P class constru even C class not having method&const
c.display()
