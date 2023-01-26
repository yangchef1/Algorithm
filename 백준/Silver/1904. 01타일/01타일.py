n = int(input())

if n != 1:
    DP = [0] * n
    DP[0] = 1
    DP[1] = 2

    for i in range(2, n):
        DP[i] = (DP[i-1] + DP[i-2]) % 15746

    print(DP[n-1])
else:
    print(1)