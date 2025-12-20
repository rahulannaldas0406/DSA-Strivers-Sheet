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

# arr=[1,2,3,4,5]

# arr[-1]=6
# print(arr)


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


arr={1,2,3,4}
arr1={4,5,6,7}

