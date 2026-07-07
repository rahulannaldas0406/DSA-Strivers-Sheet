#Find the Smallest Divisor Given a Threshold

'''Problem Statement: You are given an array of integers 'arr' and an integer i.e. a threshold value 'limit'. 
Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given array by it, 
the sum of the division's result is less than or equal to the given threshold value.'''



'''arr=[8,4,2,3]                                       
limit=10                                            
                                                    
left=1                                              
right=max(arr)                                      
ans=-1                                              
                                                    
while left<=right:

    mid=(left+right)//2
    res=0

    for i in range(len(arr)): 

        res += (arr[i]+mid-1)//mid

    # for i in range(left,right+1):
    #     sum=
    #     res=res+sum

    if res<=limit:
        ans=mid
        right=mid-1
    else:
        left=mid+1

print(ans)'''




'''arr=[4,7,9,10]
c=0
k=1
st=[]
for i in range(1,max(arr)):
    if i not in arr:
        c+=1
        st.append(i)
    
if c==0:
    print(max(arr)+k)
else:
    print(st[k-1])
print(st)'''



'''Kth Missing Positive Number

Problem Statement: You are given a strictly increasing array ‘vec’ and a positive integer 'k'. Find the 'kth' positive integer missing from 'vec'.'''



#correct version 

'''arr = [4, 7, 9, 10]
k = 4
st = []
i = 1

while len(st) < k:
    if i not in arr:
        st.append(i)
    i += 1

print(st[k - 1])
print(st)'''


'''def findKthMissingBinary(vec, k):
    left, right = 0, len(vec) - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Calculate missing numbers up to vec[mid]
        missing_count = vec[mid] - (mid + 1)
        
        if missing_count < k:
            left = mid + 1
        else:
            right = mid - 1
            
    # The answer is k + the number of elements before the insertion point
    # which is effectively k + left
    return k + left

# Test
vec = [4, 7, 9, 10]
k = 4
print(findKthMissingBinary(vec, k)) # Output: 5'''


'''class Solution:
    def removeCoveredIntervals(intervals):
        # Sort by start ascending, then by end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        max_end = 0
        
        for start, end in intervals:
            if end > max_end:
                count += 1
                max_end = end
        
        return count
    
    
arr=[[1,4],[3,6],[2,8]]
print(Solution.removeCoveredIntervals(arr))'''

#Agression Cows 

'''what i understood this problem is we have write the code in two function one is normal two linear serach but for optimal we have to apply binary search
Here is two different appraoches there 
'''

#Brute force approach 

#Algorithm

'''
->Sort the array in increasing order 
->check the every possible distance with using for loop
->for each distance call CanWePlace() function to see if all cows can be placed 
     if CanWePlace() function return false,return the current distance -1 means previous distance that was the largest where it is possible place 
->if the loop pass without failure,return the largest possible distance (differece between farthest and nearest stalls)
'''

#code

'''class Solution:

    def CanWePlace(self,nums,cows,d):
        count=1
        lastPos=nums[0]
        for i in range(len(nums)):
            if nums[i]-lastPos>=d:
                count+=1    
                lastPos=nums[i]
            if count>=cows:
                return True
        return False
    
    def aggresiveCows(self,nums,cows):
        nums.sort()

        maxDist=nums[-1]-nums[0]
        ans=0
        for d in range(1,maxDist+1):
            if self.CanWePlace(nums,cows,d):
                ans=d
        return ans
    
nums=[0,3,4,7,10,9]
cows=4  
obj=Solution()
print(obj.aggresiveCows(nums,cows))'''

#Time complexity:O(min-max)*O(n) Sometimes min-max could be fill with entire array so consider O(n)*O(n) around O(n^2)
#Space Complexity:O(1)

#Optimal Solution

#Algorithm 

'''
->same as brute force approach but small change in aggressive function in place of min-max for loop rewrite the binary search let me explain in detail
--->The main Idea of binary search is remove half of elements which we didn't want based on condition ,this minimizing the unneccessary checks
--->The answer is space is sorted:1 to we differece between min and max to we use divide into two parts :
------>One containing Valid answers
------>the other containing Non-valid answers
'''

#code

'''class Solution:

    def CanWePlace(self,nums,cows,d):
        count=1
        lastPos=nums[0]

        for i in range(1,len(nums)):
            if nums[i]-lastPos>=d:
                count+=1
                lastPos=nums[i]
            if count>=cows:
                return True
        return False
    

    def agressionCows(self,nums,cows):
        nums.sort()
        low=0
        high=nums[len(nums)-1]

        while low<=high:
            mid=(low+high)//2
            if self.CanWePlace(nums,cows,mid):
                low=mid+1
            else:
                high=mid-1

        return high
    
nums=[0,3,4,7,10,9]
cows=4
obj=Solution()
print(obj.agressionCows(nums,cows))'''

#Time complexity:O(NlogN) + O(N * log(max(stalls[])-min(stalls[])))
#space complexity:O(1)
