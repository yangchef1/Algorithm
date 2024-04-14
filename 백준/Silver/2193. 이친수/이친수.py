n = int(input())
DP = [[0] * (n + 1) for _ in range(2)]
DP[1][1] = 1

for i in range(2, n + 1):
    DP[1][i] = DP[0][i-1]
    DP[0][i] = DP[1][i-1] + DP[0][i-1]
    
print(DP[0][n] + DP[1][n])