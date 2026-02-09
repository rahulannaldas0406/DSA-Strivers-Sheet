numRows=5
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
print(triangle)