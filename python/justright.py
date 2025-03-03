arr=[1,3,2,4,6,5]
count=0
for i in range(0,len(arr)-1):
    if arr[i]<arr[i+1]:
       count=count+1
print(count)