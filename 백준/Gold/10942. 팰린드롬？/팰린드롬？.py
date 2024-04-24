n = int(input())
seq = [0] + list(map(int, input().split()))
m = int(input())
DP = [[0] * (n + 1) for _ in range(n + 1)]
result = []

for i in range(1, n + 1):
    DP[i][i] = 1
    DP[i - 1][i] = 1 if seq[i - 1] == seq[i] else 0
        
for i in range(2, n):
    for j in range(1, n - i + 1):
        DP[j][j + i] = 1 if DP[j + 1][j + i - 1] == 1 and seq[j] == seq[j + i] else 0

for _ in range(m):
    a, b = map(int, input().split())
    result.append(DP[a][b])
    
print("\n".join(map(str, result)))