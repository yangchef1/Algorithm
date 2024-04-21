t = int(input())
result = []
DP = [0] * (1000001)
DP[1], DP[2], DP[3] = 1, 2, 4
max_n = 4

for _ in range(t):
    n = int(input())
    if max_n > n:
        result.append(DP[n])
    else:
        for i in range(max_n, n + 1):
            DP[i] = (DP[i - 1] + DP[i - 2] + DP[i - 3]) % 1000000009
        result.append(DP[n])
    max_n = max(max_n, n)
    
print("\n".join(map(str, result)))