#problem is given array is [2,3,3,2]
#remove  element 3 and put in place of _ (underscore)
#like [2,2,_,_]

'''arr=[2,3,3,2,3,4,2,3]
k=3
#write like merge sort

i=0
j=0

while i<len(arr):
    if arr[i]!=k:
        arr[j]=arr[i]
        j+=1
    i+=1

while j<len(arr):
    arr[j]=None
    j+=1


print(arr)'''

'''nums=[1,3,5,6]  
target=6
low=0
high=len(nums)-1
while low<=high:
    mid=low+high//2
    if nums[mid]==target:
        print(mid)   
        break
    elif nums[mid]<target:
        low=mid+1
    else:
        high=mid-1'''