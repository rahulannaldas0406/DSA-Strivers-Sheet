#Peak element in Array

#Problem Statement: Given an array of length N, peak element is defined as the element greater than both of its neighbors.
#  Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i]. Find the index(0-based) of a peak element in the array. 
# If there are multiple peak numbers, return the index of any peak number.

arr=[1,2,3,4,5,6,7,8,5,1]

max=arr[0]
ind=0
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
        ind=i
print(ind)