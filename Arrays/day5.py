

# def problem(nums):
#     seen=set()
#     for i in nums:
#         if i in seen:
#             return i
#         seen.add(i)
    
# print(problem([1,2,1,3,1,4]))

# print(min(8,7))
arr=[10,11,13,14,15]

k=int(input("enter a how many times to  rotate elements:"))
side=str(input("enter side of rotate an array:"))

k = k % len(arr) 

if side=="left":
    while k>0: 
        first=arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]
        arr[-1]=first
        k-=1
else:
    while k>0:
        first_element=arr[-1]
        for i in range(len(arr)-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=first_element
        k-=1

print(arr)