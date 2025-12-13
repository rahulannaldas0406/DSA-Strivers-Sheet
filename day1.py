#Largest Element


'''Before start problem 
   1)Sample Examples
   2)Brute force 
   3)Optimal Approach'''
#We can solve using other sorting tech but to optimize code is this right way

'''def largestElement(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    return nums[len(nums)-1]
print("It is A largest Element:",largestElement([3,5,7,2,1]))'''


#Second Largest Element 

'''Given an array of integers nums, return the second-largest element in the array.
If the second-largest element does not exist, return -1.'''


'''def secondLargestElement(nums):
    large=-1
    sec_lar=-1
    for i in nums:
        if i>large:
            sec_lar=large
            large=i
        elif i>sec_lar and i< large:
            sec_lar=i
    return sec_lar

print(secondLargestElement([8,5,6,7]))'''

 

