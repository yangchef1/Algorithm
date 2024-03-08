n = int(input())

DP = [0 for _ in range(n+1)]
DP[0] = 4

for i in range(1, n+1):
    DP[i] = DP[i-1] + 2*(2**(i-1))*(2**(i-1) + 1) + 4**(i-1)

print(DP[n])