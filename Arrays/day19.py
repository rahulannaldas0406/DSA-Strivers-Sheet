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

arr = [4, 7, 9, 10]
k = 4
st = []
i = 1

while len(st) < k:
    if i not in arr:
        st.append(i)
    i += 1

print(st[k - 1])
print(st)