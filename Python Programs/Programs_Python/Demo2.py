#Sorting

arr=list(map(int,input().split()))
arr.sort()
print("ascending: ")
print(*arr,sep=' ')
arr.sort(reverse = True)
print("descending: ")
print(*arr,sep=' ')