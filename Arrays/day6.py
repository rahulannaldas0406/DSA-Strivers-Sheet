'''Union of Two Sorted Arrays

Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

The union of two arrays can be defined as the common and distinct elements in the two arrays.

NOTE: Elements in the union should be in ascending order.'''

#Test cases for this problem 

'''Input:n = 5,m = 5 arr1[] = {1,2,3,4,5}  arr2[] = {2,3,4,4,5}
Output: {1,2,3,4,5}
Explanation: Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1
Distnict Elemennts in arr2 are : No distinct elements.
Union of arr1 and arr2 is {1,2,3,4,5}

Input:n = 10,m = 7,arr1[] = {1,2,3,4,5,6,7,8,9,10}arr2[] = {2,3,4,4,5,11,12}
Output: {1,2,3,4,5,6,7,8,9,10,11,12}
Explanation: Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1,6,7,8,9,10
Distnict Elemennts in arr2 are : 11,12
Union of arr1 and arr2 is {1,2,3,4,5,6,7,8,9,10,11,12}'''

'''arr1=[1,2,3,4]
arr2=[3,4]
arr3=[]
k=0
i,j=0,0
while i < len(arr1) and j < len(arr2):
    if arr1[i]<arr2[j]:
        arr3[k]=arr1[i]
        k+=1
        i+=1
    elif arr1[i]>arr2[j]:
        arr3[k]=arr2[j]
        k+=1
        j+=1
    else:
        arr3[k]=arr1[i]
        k+=1
        i+=1
        j+=1

print(arr3)'''

#Find the missing number in an array




#Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. 
#Find the number(between 1 to N), that is not present in the given array..

'''arr=[2,3,4,5]
n=5
for i in range(1,n+1):
    if i not in arr:
        print(i)'''


#Count Maximum Consecutive One's in the array
#Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array..


'''def max_cons(arr):
    max_count=0
    current_count=0
    for i in range(0,len(arr)):
        if arr[i]==1:
            current_count+=1
        else:
            max_count=max(max_count,current_count)
            current_count=0
    return max(max_count,current_count)

print(max_cons([1,1,0,1,1,1]))'''


#Find the number that appears once, and the other numbers twice
#Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

# def appear_ones(arr):
#     for i in range(0,len(arr)):
#         if arr[i] in arr:
#             return arr[i]
#         break
# print(appear_ones([2,2,1]))



arr=[1,2,1,3,2]

for i in range(0,len(arr)):
    if arr[i] not in arr:
        print(arr[i])
