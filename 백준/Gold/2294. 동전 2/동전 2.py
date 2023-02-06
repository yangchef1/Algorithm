n, k = map(int, input().split())
coin = []
INF = 10001

for i in range(n):
    coin.append(int(input()))

DP = [INF for _ in range(k+1)]
DP[0] = 0

for i in coin:
    for j in range(i, k+1):
        DP[j] = min(DP[j], DP[j-i]+1)
 
if DP[k] == INF:
    print(-1)
else:
    print(DP[k])