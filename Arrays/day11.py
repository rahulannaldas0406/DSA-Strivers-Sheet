#Rotate Image by 90 degree
# Problem Statement: Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise. 
# The rotation must be done in place, meaning the input 2D matrix must be modified directly..

'''This is brute force '''


'''arr=[[1,2,3],[4,5,6],[7,8,9]]
n=len(arr)
row=len(arr)
col=len(arr)
matrix=[]
for i in range(row):
    rows = []
    for j in range(col):
        rows.append(0)
    matrix.append(rows)
print(len(arr))
print(len(matrix))

for i in range(len(arr)):
    for j in range(len(arr)):
        matrix[j][n-1-i]=arr[i][j]

for row in matrix:
    print(*row)'''


'''Better approach '''


'''arr=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(arr)):
    for j in range(len(arr)):
        if i<j:
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]

for row in arr:
    row.reverse()


for row in arr:
    print(*row)'''

