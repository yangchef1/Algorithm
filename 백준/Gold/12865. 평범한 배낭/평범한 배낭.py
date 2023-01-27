n, k = map(int, input().split())
things = [[0,0]]

for i in range(n):
    things.append(list(map(int, input().split())))
    
value = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if things[i][0] <= j:
            value[i][j] = max(value[i-1][j], value[i-1][j-things[i][0]] + things[i][1])
        else:
            value[i][j] = value[i-1][j]

print(value[n][k])   