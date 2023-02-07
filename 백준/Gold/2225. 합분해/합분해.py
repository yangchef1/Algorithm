n, k = map(int, input().split())

DP = [[1]*(k) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k):
        DP[i][j] = 0
        for l in range(i+1):
            DP[i][j] += DP[l][j-1]
            
print(DP[n][k-1] % 1000000000)