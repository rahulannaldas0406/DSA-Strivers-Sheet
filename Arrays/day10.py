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

'''this is not correct code for the problem so there is lot of drawback are there those are
Case	Works?
Single zero	✅
Multiple zeros	❌
Rectangular matrix	❌
General solution	❌'''



'''arr=[[1,1,0],[1,1,1],[1,1,1]]

for row in range(0,len(arr)):
    for col in range(0,len(arr)):
        if arr[row][col]==0:
            i=row
            j=col

for row in range(len(arr)):
    for col in range(len(arr)):
        if row==i or col==j:
            arr[row][col]=0

for row in arr:
    print(*row)'''

#The correct code is 
#This is also not 100% code it failed two test cases

'''arr=[[1,1,1],[1,1,0],[1,1,1]]
m=len(arr)
n=len(arr[0])
for row in range(m):
    for col in range(n):
        if arr[row][col]==0:
            for i in range(n):
                if arr[i][row]!=0:
                    arr[i][row]=-1
            for j in range(m):
                if arr[j][col]!=0:
                    arr[j][col]=-1
for i in range(m):
    for j in range(n):
        if arr[i][j]==-1:
            arr[i][j]=0
    
for row in arr:
    print(*row)'''

'''arr=[[1,1,1],[1,0,0],[1,1,1]]

row=[0]*len(arr[0])
col=[0]*len(arr[0])
print(row,col)
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j]==0:
            row[i]=1
            col[j]=1
for i in range(len(arr)):
    for j in range(len(arr)):
        if row[i] or col[j]:
            arr[i][j]=0
for row in arr:
    print(*row)'''

            
        