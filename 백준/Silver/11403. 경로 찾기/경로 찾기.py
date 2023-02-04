import sys

n = int(sys.stdin.readline())
INF = int(1e9)

matrix = []

for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            matrix[i][j] = INF

for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

for i in range(n):
    for j in range(n):
        if matrix[i][j] != INF:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()