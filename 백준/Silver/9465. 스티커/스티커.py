t = int(input())
result = []

for i in range(t):
    n = int(input())
    
    stick = []
    stick.append(list(map(int, input().split())))
    stick.append(list(map(int, input().split())))
    if n == 1:
        result.append(max(stick[0][0], stick[1][0]))
    elif n == 2:
        result.append(max(stick[0][1] + stick[1][0], stick[0][0] + stick[1][1]))
    else:
        DP = [[0]*n for _ in range(2)]

        DP[0][0] = stick[0][0]
        DP[1][0] = stick[1][0]
        DP[0][1] = stick[0][1] + stick[1][0]
        DP[1][1] = stick[0][0] + stick[1][1]

        for j in range(2, n):
            DP[0][j] = max(DP[1][j-1], DP[1][j-2]) + stick[0][j]
            DP[1][j] = max(DP[0][j-1], DP[0][j-2]) + stick[1][j]
        
        result.append(max(DP[0][n-1], DP[1][n-1]))
    
for i in result:
    print(i)    