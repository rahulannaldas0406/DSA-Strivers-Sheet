#Kadane's Algorithm : Maximum Subarray Sum in an Array
#Problem Statement: Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
#A subarray is a contiguous non-empty sequence of elements within an array.

'''nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max=nums[0]
max_sub=0
for i in nums:
    max_sub+=i
    #print(max_sub)
    if max_sub>max:
        max=max_sub
    if max_sub < 0:          # 👈 ONLY NEW LINE
        max_sub = 0
print(max)'''


#From neetcode platform problem 

#Linear search using hashing technique

'''def duplicate_ele(nums):
    seen=set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.append(i)
    return False

print(duplicate_ele([0,2,3]))'''