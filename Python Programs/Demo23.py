import os.path

myfile=input("Enter the file name where u want to write ?")
mf=os.path.exists(myfile)

if mf:
    f=open(myfile,"w")
    name=input("Enter the name :")
    age=input("Enter age: ")
    salary=input("Enter salary :")
    desig=input("Enter designation :")
    myrecord=[name,age,salary,desig]

    for i in myrecord:  
        f.write(i)
        f.write('\t')

    f.close()

else:
    print("Sorr file doesn't exist....!")


print("========Read======")
myfileread=input("Enter the file name where u want to read from ?")
fr=open(myfileread,"r")


for i in fr:
    print(i)
