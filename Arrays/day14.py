'''Floor and Ceil in Sorted Array

Problem Statement: ou're given an sorted array arr of n integers and an integer x. 
Find the floor and ceiling of x in arr[0..n-1]. The floor of x is the largest element in the array which is smaller than or equal to x. 
The ceiling of x is the smallest element in the array greater than or equal to x'''



'''def floor_ceil(arr,k):
    floor=0
    ceil=0
    if k in arr:
        floor=k
        ceil=k
        return floor,ceil
    if arr[0]>k:
        floor=-1
        ceil=arr[0]
        return floor,ceil
    if arr[-1]<k:
        floor=arr[-1]
        ceil=-1
        return floor,ceil
    for i in range(len(arr)):
        if arr[i]<=k:
            floor=arr[i]
        else:
            ceil=arr[i]
            break
    return floor,ceil

a=floor_ceil([2, 4, 6, 8],10)
print(a)'''

# binary approach this optimal approach 

#Approach	Time	Interview Value

'''Linear scan	O(n)	⭐ Beginner
Binary search	O(log n)	⭐⭐⭐ Must know
Python bisect	O(log n)	⭐⭐⭐ Practical
Lower bound pattern	O(log n)	⭐⭐⭐⭐ Advanced DSA'''


'''def floor_ceil(arr,k):
    n=len(arr)
    floor=-1
    ceil=-1
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=k:
            floor=arr[mid]
            low=mid+1
        else:
            ceil=arr[mid]
            high=mid+1
    return floor,ceil
a=floor_ceil([2, 4, 6, 8],10)
print(a)'''

#Last occurrence in a sorted array

#Problem Statement: Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key. 
#If the target is not found then return -1. Note: Consider 0 based indexing

'''def last_occurence(arr,k):
    res=-1
    for i in range(len(arr)):
        if arr[i]==k:
            res=i
    return res
a=last_occurence([3, 4, 13, 13, 13, 20, 40],60)
print(a)'''

#TC =O(n)
#SC =O(1)

#the above code is not optimize 

#optimize approach is Binary search 

'''def last_occurence(arr,k):
    n=len(arr)
    res=-1
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2

        if arr[mid]==k:
            res=mid
            low+=1
            high+=1
        elif arr[mid]>k:
            high-=1
        else:
            low+=1
    return res
a=last_occurence([3, 4, 13, 13, 13, 20, 40],60)
print(a)'''

'''Count Occurrences in Sorted Array

Problem Statement: You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.'''

def count_occurence(arr,k):
    count=0
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==k:
            count+=1
            low+=1
            high-=1
        elif arr[mid]<k:
            low+=1

        else:
            high-=1
    return count
a=count_occurence([2, 2 , 3 , 3 , 3 , 3 , 4],3)
print(a)