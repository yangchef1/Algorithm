a = list(input())
b = list(input())
c = list(input())

DP = [[[0]*(len(b) + 1) for _ in range(len(a) + 1)] for _ in range(len(c) + 1)]

for k in range(1, len(c)+1):
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if c[k - 1] == a[i - 1] and a[i - 1] == b[j - 1]:
                DP[k][i][j] = DP[k-1][i-1][j-1] + 1
            else:
                DP[k][i][j] = max(DP[k][i-1][j], DP[k][i][j-1], DP[k-1][i][j])

print(DP[len(c)][len(a)][len(b)])