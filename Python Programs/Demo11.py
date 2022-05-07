
#type 1
"""class Bank:
    #def abc(self,a,b):
        #print("last abc method")

    def Loan(self):
        print("Loan with 1st super bank")
    def Loan(self):
        print("Laon with 2nd super bank")#Overloading not possible (ie)- recent method only will be printed
        
#class SBI (Bank):
#    #pass
#    def Loan(self):
#       print("Loan with SBI class")#Over riding

d=Bank()#if bank class recent loan method in bank class will be printed
d.Loan()
"""        

#########################################
#tpe 2
class Bank:
    #def abc(self,a,b):
        #print("last abc method")

    def Loan(self):
        print("Loan with 1st super bank")
    def Loan(self):
        print("Laon with 2nd super bank")#Overloading not possible (ie)- recent method only will be printed
        
class SBI (Bank):
    #pass
    def Loan(self):
        print("Loan with SBI class")#Over riding

d=SBI()#if sbi, sbi child class loan will be printed
d.Loan()
