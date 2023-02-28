import sys
dp = [0] * 1000001


def number (n):
    if n == 1:
        return 0
    dp[2] = dp[3] = 1
    if dp[n] != 0:
        return dp[n]
    for i in range(4,n+1):
        if i % 3 + i % 2 == 0:
            dp[i] = min([dp[i-1],dp[i//3],dp[i//2]]) + 1
        elif i % 3 == 0 and i % 2 != 0:
            dp[i] = min([dp[i-1],dp[i//3]]) + 1
        elif i % 3 != 0 and i % 2 == 0:
            dp[i] = min([dp[i-1],dp[i//2]]) + 1
        else:
            dp[i] = dp[i-1] + 1
    return dp[n]


n = int(sys.stdin.readline())

print(number(n))