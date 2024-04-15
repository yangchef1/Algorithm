n = int(input())
t, p = [], []
DP = [0] * n
result = 0

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

DP[0] = p[0] if t[0] == 1 else 0

for i in range(1, n):
    DP[i] = max([DP[i - k - 1] + p[i - k ] if i >= k and t[i - k] == k + 1 else 0 for k in range(5)])
    DP[i] = max([DP[i - k] if i >= k else 0 for k in range(5)])

print(DP[-1])