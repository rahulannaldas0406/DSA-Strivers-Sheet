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

'''class Solution {
    public void rotateArray(int[] nums, int k) {
        while(k > 0){
            int ind0 = nums[0];
            for(int i = 1 ;i < nums.length;i++) {
                nums[i-1] = nums[i];
            }
            nums[nums.length - 1] = ind0;
            k--;
        }                               
    }
}'''

'''def leftRotate(nums,k):
    while k>0:
        indo=nums[0]
        for i in range(1,len(nums)):
            nums[i-1]=nums[i]
        nums[len(nums)-1]=indo
        k-=1
    return nums
arr=[1,2,3,4,5]
print(leftRotate(arr,2))'''

'''def leftRotate(nums,k):
    while k>0:
        indo=nums[len(nums)-1]
        nums[0]=indo
        for i in range(1,len(nums)-1):
            nums[i]=nums[i]
        nums[len(nums)-1]=indo
        k-=1
    return nums
arr=[1,2,3,4,5]
print(leftRotate(arr,2))'''



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


# arr={1,2,3,4}
# arr1={4,5,6,7}


#arr=[9,9,9] #for this test case it not work poperly so instead 
'''res=""
for i in range(0,len(arr)):
    res+=""+ str(arr[i])

num=int(res)+1
value=str(num)
for i in range(0,len(value)):
    arr[i]=int(value[i])

print(arr)'''


'''def plusOne(arr):
   n=len(arr) 
   for i in range(n-1,-1,-1):
        if arr[i]<9:
           arr[i]+=1
           return arr
        arr[i]=0

   return [1] +arr 


print(plusOne([9,9,9]))'''

# for i in range(0,len(arr)):
#     arr[i]=str(num[i])
# print(arr)