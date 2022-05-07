f=open("Emp.txt","w")##while opening this file, we can see the details what we wrote here...

name=input("Enter the name :")
age=input("Enter age: ")
salary=input("Enter salary :")
desig=input("Enter designation :")
myrecord=[name,age,salary,desig]

for i in myrecord:
    f.write(i)
    f.write('\t')

f.close()
