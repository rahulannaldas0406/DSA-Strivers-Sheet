#Binary Search: Explained
#Problem statement: You are given a sorted array of integers and a target, your task is to search for the target in the 
# given array. Assume the given array does not contain any duplicate numbers.

'''arr=[34,23,13,43]

num=23
for i in arr:
    if i ==num:
        print("true")
        break'''


'''Implement Lower Bound

Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.'''

#What is lower bound?

'''The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.'''

'''def lowerbound(arr,k):
    for i in range(len(arr)):
        if arr[i]>=k:
            return i
a=lowerbound([3,5,8,15,19],9)
print(a)'''


'''Implement Upper Bound

Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.'''

#What is Upper Bound?

'''The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than the given key i.e. x.

The upper bound is the smallest index, ind, where arr[ind] > x.'''

'''def upperbound(arr,k):
    for i in range(len(arr)):
        if arr[i]>k:
            return i
print(upperbound([1,2,2,3],2))'''



'''Search Insert Position

Problem Statement: You are given a sorted array arr of distinct values and a target value x. 
You need to search for the index of the target value in the array'''

'''def Searchinsertion(arr,k):
    for i in range(len(arr)):
        if arr[i]>=k:
            return i
print(Searchinsertion([1,2,4,7],6))'''
