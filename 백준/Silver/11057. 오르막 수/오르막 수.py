n = int(input())

DP = [[0]*n for _ in range(10)]

for i in range(10):
    for j in range(n):
        if j == 0:
            DP[i][j] = 1
        else:
            for k in range(i+1):
                DP[i][j] += DP[k][j-1]
                
sum = 0

for i in range(10):
    sum += DP[i][n-1]
    
print(sum%10007)