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

arr1=[1,2,3,4]
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

print(arr3)
