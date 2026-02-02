#Find the number that appears once, and the other numbers twice
#Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.


#arr=[1,2,1,3,2,3,4]

'''count=1
res=0
for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if arr[i]==arr[j]:
            count+=1
    if count>1:
        count=0
    else:
        res=arr[i]
print(res)'''

'''res=0
for i in arr:
    res^=i
print(res)'''



#Longest Subarray with given Sum K(Positives)
#Problem Statement: Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. 
# If no such sub-array exists, return 0


'''arr=[-3, 2, 1]
k=6
ind=0
dist=0
count=0
for i in range(0,len(arr)):
    res=arr[i]
    for j in range(i+1,len(arr)):
        res+=arr[j]
        count+=1
        if res==k:
            if count>dist:
                dist=count
                ind=j
                break
        elif res>k:
            break
        else:
            pass
print(ind)'''

def longest_ele(arr,k):
    count=1
    dist=0
    pre_sum=0
    sum=0
    i=0
    j=1
    while i<=len(arr):
        pre_sum=arr[i]+arr[j]
        if pre_sum==k:
            if count>dist:
                dist=count
                count=0
                if i==len(arr):
                    return j
        elif pre_sum>k:
            i+=1
        else:
            j+=1
arr = [1, 2, 3, 1, 1, 1, 1]
k = 3
print(longest_ele(arr,k))