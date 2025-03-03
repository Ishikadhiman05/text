arr=list(input("Enter a list: "))
print(arr)
mid=len(arr)//2
start=mid
end=len(arr)-1
while start<end:
    arr[start],arr[end]=arr[end],arr[start]
    start+=1
    end-=1
print(arr)