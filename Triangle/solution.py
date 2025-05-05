triangle = [[-1],[2,3],[1,-1,-3]]

for row in range(len(triangle) - 2, -1, -1):
    for col in range(len(triangle[row])):
        triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
print(triangle[0][0])