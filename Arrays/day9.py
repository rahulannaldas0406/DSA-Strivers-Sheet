#Kadane's Algorithm : Maximum Subarray Sum in an Array
#Problem Statement: Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
#A subarray is a contiguous non-empty sequence of elements within an array.

'''nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max=nums[0]
max_sub=0
for i in nums:
    max_sub+=i
    #print(max_sub)
    if max_sub>max:
        max=max_sub
    if max_sub < 0:          # 👈 ONLY NEW LINE
        max_sub = 0
print(max)'''


#From neetcode platform problem 

#Linear search using hashing technique

'''def duplicate_ele(nums):
    seen=set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.append(i)
    return False

print(duplicate_ele([0,2,3]))'''

#Stock Buy And Sell
#Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day. 
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. 
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


'''arr=[7,6,4,3,1]

profit=0
curr_profit=0
mini=arr[0]
sel=0
for i in arr:
    if i<mini:
        mini=i
    else :
        curr_profit=i-mini
        if curr_profit>profit:
            profit=curr_profit
print(profit)'''

#Rearrange Array Elements by Sign
#Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. 
# Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

'''for i in arr:
    if i<0:
        neg[n]=i
        n+=1
    else:
        pos[p]=i
        p+=1'''


'''arr=[1,2,-4,-5]

pos=[]
neg=[]
p=0
n=0
i=0

while i<len(arr):
    if arr[i]>0:
        pos.append(arr[i])
    else:
        neg.append(arr[i])
    i+=1

j=0
while j<len(arr):
    if j%2==0:
        arr[j]=pos[p]
        p+=1
    else:
        arr[j]=neg[n]
        n+=1
    j+=1
print(arr)'''


#Leaders in an Array  

'''arr= [10, 22, 12, 3, 0, 6] 
i=0
j=i+1

while i<len(arr):
    if i==len(arr)-1:
        print(arr[i])
        break
    
    if arr[i]>arr[j]:
        j+=1
    
    else:
        i+=1
        j=i+1
    if j==len(arr):
        print(arr[i],end=" ")
        i+=1
        j=i+1'''


mat=[[1,1,1],[1,0,1],[1,0,0]]

print(mat)