#Find the number that appears once, and the other numbers twice
#Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.


arr=[2,2,3,2]

count=1
res=0
for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if arr[i]==arr[j]:
            count+=1
    if count>1:
        count=0
    else:
        res=arr[i]
print(res)

# res=0
# for i in arr:
#     res^=i
# print(res)


#Longest Subarray with given Sum K(Positives)
#Problem Statement: Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. 
# If no such sub-array exists, return 0


arr=[10, 5, 2, 7, 1, 9]
k = 15
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
print(ind)

'''barr = [10, 5, 2, 7, 1, 9]
k = 15

left = 0
curr_sum = 0
max_len = 0
end_index = -1

for right in range(len(arr)):
    curr_sum += arr[right]

    while curr_sum > k:
        curr_sum -= arr[left]
        left += 1
    print(curr_sum)  

    if curr_sum == k:
        length = right - left + 1
        if length > max_len:
            max_len = length
            end_index = right

# print(end_index)'''

    
'''def longest_ele(arr,k):
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
print(longest_ele(arr,k))'''