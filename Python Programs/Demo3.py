for i in range(10):#range from 0 to 9
    print(i)

for i in range(1,10):#range from 1 to 9
    print(i)

for i in range(0,5):#range from 0 to 4
    print(i,end=" ")#in a single line with space

print("========")

start=int(input("Enter start number: "))
myrange=int(input("Enter myrange number: "))
incre=int(input("Enter incre number: "))

for i in range(start,myrange,incre):#getting range from user
    print(i)
print("======for with if====")
for i in range(20):
    if(i%2==0):
        print("Even :",i)
          
          
