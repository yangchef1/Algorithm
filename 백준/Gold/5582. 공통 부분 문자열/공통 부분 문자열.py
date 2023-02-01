import sys

a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())
DP = [[0]*(len(b) + 1) for _ in range(len(a) + 1)]
result = 0

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
            result = max(result, DP[i][j])
            
print(result)