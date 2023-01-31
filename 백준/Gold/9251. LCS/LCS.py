a = list(input())
b = list(input())
DP = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
            
print(DP[len(a)][len(b)])