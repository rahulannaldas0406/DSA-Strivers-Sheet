#Longest Consecutive Sequence in an Array
#Problem Statement: Given an array nums of n integers.
#Return the length of the longest sequence of consecutive integers. The integers in this sequence can appear in any order.

'It is better solution for the problem  not optimize code'


'''arr=[0,3,7,2,5,8,4,6,0,1]
arr.sort()
curr_count=1
longest=1
last_element=None
for i in range(0,len(arr)):
    if arr[i]-1==last_element:
        curr_count+=1
        last_element=arr[i]
    elif arr[i]!=last_element:
        curr_count=1
        last_element=arr[i]
    longest=max(longest,curr_count)
print(longest)'''


'for optimize solution you need to follow the below steps'

# 0+1 is exist or not ? if exist count+=1 and num=num+1 else return count
# num+1 is exist or not ? if 


#Set Matrix Zero
#Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to 
# set its entire column and row to 0 and then return the matrix..

