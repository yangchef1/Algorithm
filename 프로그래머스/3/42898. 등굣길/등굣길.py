def solution(m, n, puddles):
    DP = [[0] *(m+1) for _ in range(n+1)]
    DP[1][1] = 1
    
    for x in range(1, n+1):
        for y in range(1, m+1):
            if (x != 1 or y != 1) and [y, x] not in puddles:
                DP[x][y] = DP[x-1][y] + DP[x][y-1]
    
    return DP[n][m] % 1000000007