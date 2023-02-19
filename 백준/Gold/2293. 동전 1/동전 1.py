import sys

n, k = map(int, sys.stdin.readline().split())
coin = []

for i in range(n):
    coin.append(int(sys.stdin.readline()))

DP = [0 for _ in range(k+1)]
DP[0] = 1

for i in coin:
    for j in range(i, k+1):
            DP[j] += DP[j-i]
    
            
print(DP[k])