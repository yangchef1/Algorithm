def solution(triangle):
    DP = triangle
    for line in range(1, len(DP)):
        for i in range(len(DP[line])):
            if i - 1 < 0:
                DP[line][i] += DP[line-1][i]
            elif i >= line:
                DP[line][i] += DP[line-1][i-1]
            else:
                DP[line][i] += max(DP[line-1][i-1], DP[line-1][i])
                
    return max(DP[-1])