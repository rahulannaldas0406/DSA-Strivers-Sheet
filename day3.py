#Left Rotate the Array by One

'''Example 1:
Input:
 nums = [1, 2, 3, 4, 5]  
Output:
 [2, 3, 4, 5, 1]  
Explanation:
 Initially, nums = [1, 2, 3, 4, 5]  
Rotating once to the left results in nums = [2, 3, 4, 5, 1].

Example 2:
Input:
 nums = [-1, 0, 3, 6]  
Output:
 [0, 3, 6, -1]  
Explanation:
 Initially, nums = [-1, 0, 3, 6]  
Rotating once to the left results in nums = [0, 3, 6, -1].'''

'''def left_rotate_array(n):
    arr=n
    j=0
    first_index=arr[0]
    for i in range(1,len(arr)+1):
        if i==len(arr):
            arr[j]=first_index
        else:
            arr[j]=arr[i]
            j+=1
    return arr
a=[1,2,3,4,5]
print(left_rotate_array(a))'''

#To more optimization code

'''def left_rotate_array(arr):
    first = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[-1] = first
    return arr

a = [1,2,3,4,5]
print(left_rotate_array(a))'''


#Move all Zeros to the end of the array



3

#Problem Statement: You are given an array of integers, your task is to move all the zeros 
#in the array to the end of the array and move non-negative integers to the front by maintaining their order.

'''arr=[1,0,2,0,3]
j=0
count=0
for i in range(0,len(arr)):
    if arr[i]!=0:
        arr[j]=arr[i]
        j+=1
    else:
        count+=1
        n=len(arr)-count
        arr[n]=arr[i]

print(arr)'''

'''arr=[1,0,2,0,3]

pos=0
for i in range(0,len(arr)):
    if arr[i]!=0:
        arr[pos]=arr[i]
        pos+=1

for j in range(pos,len(arr)):
    arr[j]=0
print(arr)'''


#Linear Search in C

#Problem Statement: Given an array, and an element num the task is to find 
#if num is present in the given array or not. If present print the index of the element or print -1.

def liner_search(arr,k):
    n=len(arr)
    value=k
    for i in range(0,n):
        if arr[i]==value:
            return i
        
    return -1
a=[2,3,4,1]
print(liner_search(a,5))