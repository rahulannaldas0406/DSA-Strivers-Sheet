#something gone wrong

# N=int(input())
# arr=list(map(int,input().split()))
# res=0
# for i in arr:
#     res^=i

# print(res)

arr=[2,4,9,3]
res=[0]*len(arr)

window_sum=0
# k=2
# for i in range(1,k+1):
#     window_sum+=arr[i]

# res[0]=window_sum

# for i in range(k+1,len(arr)+k):

#     window_sum=window_sum-arr[(i-k)%len(arr)]+arr[i%len(arr)]
#     res[i-k]=window_sum
# print(res)
# k=-2
# for i in range(1,abs(k)+1):
#     window_sum+=arr[(0-i)%4]
# print(window_sum)

# for i in range(1,len(arr)-1):
#     window_sum=window_sum-arr[(i+k-1)%len(arr)]+arr[(i-1)%len(arr)]
#     res[i]=window_sum
# 0 1 2 3
# 0
# print((0-1)%4)#3
# print((0-2)%4)#2 #rem
# 1
# print((0-2)%4) #2
# print() to get rem what should i do 
# print((1+2-1)%4)
# print((1-1)%4)


# s="abcabc"
# for i in range(3):
#     window_str=

# arr = [8, 2, 4, 5, 3, 7, 1]
# n=len(arr)+1
# expsum=n*(n+1)//2
# print(expsum)
# print(sum(arr))

#Serialization/Deserialization neet code Encode and decode
# arr=[2,4,2,4,3,1]
# arr1=[]
# p_sum=0
# max_sum=0
# for i in arr:
#     if i not in arr1:
#         p_sum+=i
#         arr1.append(i)
#     else:
#         max_sum=max(p_sum,max_sum)
#         arr1=[]
#         p_sum=0
#         p_sum+=i
#         arr1.append(i)
# print(max_sum)

'''from collections import deque
from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Dictionary to map original nodes to their clones
        # Key: original node, Value: cloned node
        visited = {}
        
        # Initialize the queue with the starting node
        queue = deque([node])
        
        # Create the clone for the starting node and add to visited map
        visited[node] = Node(node.val)
        
        while queue:
            current = queue.popleft()
            
            # Iterate through neighbors of the current node
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    # If neighbor hasn't been cloned yet, create a clone
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # Add the cloned neighbor to the current node's clone neighbors
                visited[current].neighbors.append(visited[neighbor])
        
        # Return the clone of the starting node
        return visited[node]'''
        