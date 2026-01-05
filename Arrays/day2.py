#Check if an Array is Sorted 

'''Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: True.
Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.
'''

'''def check_sort(arr):
    value=False
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):      # compare until unsorted part
            if arr[j] < arr[j+1]:  # compare adjacent elements
                value=True
            else:
                value=False
                break
    return value
print(check_sort([1,2,3,4]))'''

#I use bubble sort to solve this problem so the chatgpt gave few drawbacks and it gives a new optimization code 

'''def check_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
print(check_sort([1,2,3,4]))'''

#Remove Duplicates in-place from Sorted Array

'''Input: arr[]=[1,1,2,2,2,3,3]
Output: [1,2,3,_,_,_,_]
Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.
Input: arr[]=[1,1,1,2,2,3,3,3,3,4,4]
Output: [1,2,3,4,_,_,_,_,_,_,_]
Explanation: Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] in the beginning of the array.'''

'''arr=[1,1,2,2,3,3,4,4,5]
arr1=[0]*len(arr)
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]!=arr[j]:
            arr1.append(arr[i])
print(arr1)'''

'''def removeDuplicates(ar):
    if len(ar) == 0:
        return 0

    k = 1  # position for next unique element

    for i in range(1, len(ar)):
        if ar[i] != ar[i - 1]:
            ar[k] = ar[i]
            k += 1

    return k
arr=[1,1,2,2,3,4,4]
k=removeDuplicates(arr)
print(arr[:k])'''

# pairs = {(i, j) for i in range(1, 3) for j in range(1, 3)}
# print(pairs)

