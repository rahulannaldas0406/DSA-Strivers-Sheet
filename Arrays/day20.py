#Allocate Minimum Number of Pages
# Rules
#  Each student gets at least one book.
#  Each book should be allocated to only one student.
#  Book allocation should be in a contiguous manner.

'''class Solution:
    def allocatePages(self,arr,k,mid):
        self.k=k
        self.arr=arr
        self.mid=mid
        st=1
        res=0

        for i in range(len(arr)):
            if res+arr[i]<=mid:
                res+=arr[i]
            else:
                st+=1
                res=arr[i]
                
        
        if st<=k:
            return True
        else:
            return False


    def binarySearch(self,arr,k):
        arr.sort()
        
        low=arr[0]
        high=sum(arr)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if self.allocatePages(arr,k,mid):
               high=mid-1
               
            else:
                low=mid+1
                ans=low
        return ans

arr=[12,34,67,90]
k=2
obj=Solution()
print(obj.binarySearch(arr,k))'''

# arr=[1,2,3,4]
# arr.reverse()
# print(arr)

s = "the sky is blue"
arr=s.split()
arr.reverse()
print(" ".join(arr).strip())







'''Next Permutation

1. Traverse from right.
2. Find first index i where nums[i] < nums[i+1].
   -> breakpoint

3. Find the smallest element greater than nums[i]
   on the right side.

4. Swap them.

5. Reverse everything after i.

Special case:
If no breakpoint exists,
reverse the whole array.'''

'''arr=[1,2,3]
ind=len(arr)-2
for i in range(len(arr)-1,-1,-1):
    if arr[ind]<arr[i]:
        bp=arr[ind]
        break
    else:
        ind-=1

greater=bp
for i in range(ind,len(arr)):
    if arr[i]>bp:
        greater=arr[i]
        ind1=i

#Swap doing 
arr[i],arr[ind1]=arr[ind1],arr[i]
print(arr)'''

