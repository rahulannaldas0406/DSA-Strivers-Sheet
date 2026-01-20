#Two Sum : Check if a pair with given sum exists in Array
#Problem Statement: Given an array of integers arr[] and an integer target.
#1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
#2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

#This is the logic for the problem should be prepared


def Twosum(arr,target):
    for i in range(0,len(arr)):
        need=target-arr[i]
        if need in arr:
            return True
    return False

print(Twosum([2,6,5,11],14))


#Sort an array of 0s, 1s and 2s
#Problem Statement: Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. 
# The sorting must be done in-place, without making a copy of the original array.

#arr = [1, 0, 2, 1, 0]
'''arr=[0, 0, 1, 1, 1]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

print(arr)'''

'''“First, I can solve it using three temporary arrays to group 0s, 1s, and 2s.
This runs in O(n) time but uses extra space.
To optimize space, I can do the same grouping in-place using three pointers (Dutch National Flag).”'''

#This is my logic but here is almost correct until time complexity but when checking space complexity checks it had extra space so to solve the problem 

#my thinking is :“I’ll take boxes, put balls in correct boxes, then arrange boxes”

#think like this :“I’ll rearrange balls inside the same box without using extra boxes” 
'''arr = [1, 0, 2, 1, 0]

left = []
middle = []
right = []

for x in arr:
    if x == 0:
        left.append(x)
    elif x == 1:
        middle.append(x)
    else:   # x == 2
        right.append(x)

result = left + middle + right
print(result)'''

#Find the Majority Element that occurs more than N/2 times
#Problem Statement: Given an integer array nums of size n, return the majority element of the array.
#The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.

arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]



