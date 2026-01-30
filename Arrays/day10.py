#Longest Consecutive Sequence in an Array
#Problem Statement: Given an array nums of n integers.
#Return the length of the longest sequence of consecutive integers. The integers in this sequence can appear in any order.

arr=[0,3,7,2,5,8,4,6,0,1]
count =1
num=min(arr)

for i in range(0,len(arr)):
    if num+1 in arr:
        count+=1
        num=num+1
    else:
        print(count)
        break

# 0+1 is exist or not ? if exist count+=1 and num=num+1 else return count
# num+1 is exist or not ? if 
