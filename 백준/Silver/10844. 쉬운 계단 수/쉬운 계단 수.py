n = int(input())

DP = [[0]*10 for _ in range(n)]
DP[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            DP[i][j] = DP[i-1][1]
        elif j == 9:
            DP[i][j] = DP[i-1][8]
        else:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1]

sum = 0
for i in range(10):
    sum += DP[n-1][i]

print(sum % 1000000000)