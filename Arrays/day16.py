#Minimum in Rotated Sorted Array

#Problem Statement:
'''Given an integer array arr of size N, sorted in ascending order (with distinct values), the array is rotated at any index which is unknown. 
Find the minimum element in the array.

Pre-requisites: Search in Rotated Sorted Array I,  Search in Rotated Sorted Array II & Binary Search algorithm'''

'''arr=[4,5,6,7,0,1,2,3]
res=arr[0]
for i in range(len(arr)):
    if arr[i]<=res:
        res=arr[i]
print(res)'''

#Find out how many times the array has been rotated

'''Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). 
Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated.

Pre-requisites: Find minimum in Rotated Sorted Array,  Search in Rotated Sorted Array II & Binary Search algorithm'''

'''arr=[15,18,2,3,6,12]
res=arr[0]
index=0
for i in range(len(arr)):
    if arr[i]<=res:
        res=arr[i]
        index=i
print(index)'''

#Search Single Element in a sorted array

'''Problem Statement: Given an array of N integers. Every number in the array except one appears twice. 
Find the single number in the array.'''

arr= [1,1,2,2,3,3,4,5,5,6,6]
res=0
for i in arr:
    res^=i
print(res)

#Peak element in Array

'''Problem Statement: Given an array of length N, peak element is defined as the element greater than both of its neighbors. 
Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i]. Find the index(0-based) of a peak element in the array. 
If there are multiple peak numbers, return the index of any peak number.'''
