import os.path

myfile=input("Enter File Name: ")
mf=os.path.exists(myfile)

class emp:
    def create(self,ch1):
        if mf:
            f = open(myfile,"w")
            self.uid=input("Enter Id: ")
            self.name = input("Enter Name: ")
            self.age=input("Enter Age: ")
            self.salary=input("Enter Salary: ")
            
            if(ch1==1):
                self.desig = "Clerk"
            elif(ch1==2):
                self.desig = "Programmer"
            elif(ch1==3):
                self.desig = "Developer"
            elif(ch1==4):
                self.desig = "Manager"
            else:
                self.desig = "Invalid Input"
            m = [self.uid, self.name, self.age, self.salary, self.desig]
            for i in m:
                f.write(i)
                f.write("\t")
            f.close()
            
    def display(self):
        print("Id :",self.uid)
        print("Name :",self.name)
        print("Age :",self.age)
        print("Salary :",self.salary)
        print("Designation :",self.desig)
        
    def raisesal(self):
        print("Id :",self.uid)
        print("Name :",self.name)
        print("Age :",self.age)
        print("Salary :",self.salary+20000)
        print("Designation :",self.desig)

            
print("Hi...Welcome...!")
ch=0

e = emp()

    
if mf:
    while(ch!=5):
        ch = int(input("MENU\n 1.Create\n 2.Display\n 3.RaiseSal\n 4.Exit\n"))
        if(ch==1):
            ch1 = int(input("MENU\n 1.Clerk\n 2.Programmer\n 3.Developer\n 4.Manager\n 5.Exit\n"))
            e.create(ch1)     
        elif(ch==2):
            e.display()
        elif(ch==3):
            e.raisesal()
        elif(ch==4):
            break
        else:
            print("Invalid Input")
        

else:
    print("Sorry...File Not Found...")
    
mfr=input("Enter File Name: ")
fr=open(mfr,"r")

for i in fr:
    print(i)
