#Allocate Minimum Number of Pages
# Rules
#  Each student gets at least one book.
#  Each book should be allocated to only one student.
#  Book allocation should be in a contiguous manner.












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

