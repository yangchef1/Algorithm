import sys

m, n = map(int, sys.stdin.readline().split())
INF = int(1e9)

matrix = [[INF]*m for _ in range(m)]

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

for k in range(m):
    for i in range(m):
        for j in range(m):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

result = []
for i in range(m):
    sum = 0
    for j in range(m):
        sum += matrix[i][j]
    result.append(sum)

print(result.index(min(result)) + 1)