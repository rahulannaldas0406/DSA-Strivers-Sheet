#Finding Sqrt of a number using Binary Search

#Problem Statement: You are given a positive integer n. 
# Your task is to find and return its square root. If ‘n’ is not a perfect square, then return the floor value of sqrt(n).

'''from math import sqrt


print(round(sqrt(28)))'''

# can solve without import any lib

#How ? look here,

'''def sqrt_poztv(n):
    low=0
    high=n
    while low<=high:
        mid=(low+high)//2
        if mid *mid==n:
            return mid
        elif mid*mid<n:
            low=mid+1
        else:
            high=mid-1
    return high
print(sqrt_poztv(25))'''

#Nth Root of a Number using Binary Search

#Problem Statement: Given two numbers N and M, find the Nth root of M. 
# The nth root of a number M is defined as a number X when raised to the power N equals M. 
# If the 'nth root is not an integer, return -1.

# def findNroot(n,m):
#     res=0
#     a=False
#     while a

        
#     return -1
# print(findNroot(3,27))

'''n=5
m=32
left=1
right=27
while left<=right:
    mid=left+(right-left)//2
    if mid**n==m:
        print(mid)
        break
    elif mid**n>m:
        right=mid-1
    else:
        left=mid+1
else:
    print("-1")'''




    
