'''numRows=5
triangle = []

if numRows >= 1:
    triangle.append([1])

if numRows >= 2:
    triangle.append([1, 1])

for i in range(2, numRows):
    prev = triangle[i - 1]
    row = [1]

    for j in range(1, len(prev)):
        row.append(prev[j - 1] + prev[j])

    row.append(1)
    triangle.append(row)
print(triangle)'''

'''triangle=[[-1],[-2,-3]]
count=0
res=0
for row in triangle:
    res+=min(row)
print(res)'''

#Single Number II Problem med

'''def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        count=1
        res=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count>1:
                count=0
            else:
                res=nums[i]
        return res'''
'''nums=[3,6,9,1]
nums.sort()
diff=0
res=nums[1] - nums[0]
i=0
j=1
while j<len(nums):
    diff=nums[j]-nums[i]
    if res>diff:
        res=diff
    i+=1
    j+=1
print(res+1)'''

n=11
count=0
while n>0:
    res=n%2
    print(res)
    if res==1:
        count+=1
    n=n//2
print(count)