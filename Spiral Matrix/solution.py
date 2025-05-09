matrix = [[1,2,3],[4,5,6],[7,8,9]]

x = len(matrix) * len(matrix[0])
c = []
while matrix:
    c.extend(matrix[0])
    # print(c)
    matrix = list(zip(*matrix[1:]))[::-1]

print(c)
