#append

print("1  =============")

data=[10,20,30,40,50]

total=0

for i in data:
    total=total+i#finding sum 
print("Total:",total)


###storing in another list also
print("2  ===========")

data1=[]
for i in data:
    if i not in data1:
        data1.append(i)

print(data)
print(data1)

print("3  =============")

howmanyemp=int(input("Enter Emp Count :"))
myemp=[]
for i in range(howmanyemp):
    myemp.append(input("Enter name: "))
print(" =========")
for i in myemp:
    print(i)

print("========")
myemp.remove("Raj")
print(myemp)
