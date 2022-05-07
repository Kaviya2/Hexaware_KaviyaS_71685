##list and set

list1=[10,20,30,40,50,60,60]
print(list1)
print(type(list1))
##Set - not allow dup and no user entered order
data={10,20,30,40,50,60,60}
print(data)
print(type(data))

data.add(100)
data.remove(20)
data.pop()

for i in data:
    print(i)

print("======")
##for order - sorting
print("Before sorting :",data)
mydata=sorted(data)
print("After Sorting :",mydata)
