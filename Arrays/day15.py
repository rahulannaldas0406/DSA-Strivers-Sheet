#Search Element in a Rotated Sorted Array

#Problem Statement: Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. 
# The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.

'''def binary(nums,target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

           
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
 
            
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

a=binary([4,5,6,1,2,3],9)
print(a)'''

#Search Element in Rotated Sorted Array II

#Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. 
# Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.

'''def search(nums, target):

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            # duplicate case (important new step)
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # left half sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # right half sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False
a=search([1,0,1,1,1],0)
print(a)'''

