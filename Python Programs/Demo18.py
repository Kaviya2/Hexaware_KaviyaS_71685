#Collection Demo
#list
# [ ] -square bracket

data=[10,20,30,40,50,60,70,80,90,100]
print(data)
print(type(data))
print(data[2:5])
data.append(200)
print(data)
print("Max :",max(data))
print("Min :",min(data))
print("Length :",len(data))
print(data)
print("Pop:",data.pop())
print(data)
data.insert(3,"A")
print(data)

data.remove(50)
print(data)

data.reverse()
print(data)


###Tuple

##() - circular bracket
print("=====tuple=====")
data1=(10,20,30,40,50,60,70,80,90,100)
print(data1)
print(type(data1))
