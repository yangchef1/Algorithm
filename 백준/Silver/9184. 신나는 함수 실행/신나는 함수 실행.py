DP = [[[0]*21 for _ in range(21)] for _ in range(21)]
result = []

for i in range(21):
    for j in range(21):
        DP[0][i][j] = 1
        DP[i][0][j] = 1
        DP[i][j][0] = 1 
               
for i in range(21):
    for j in range(21):
        for k in range(21):
            if DP[i][j][k] == 0:
                if i < j and j < k:
                    DP[i][j][k] = DP[i][j][k-1]  + DP[i][j-1][k-1] - DP[i][j-1][k]
                else:
                    DP[i][j][k] = DP[i-1][j][k] + DP[i-1][j-1][k] + DP[i-1][j][k-1] - DP[i-1][j-1][k-1]

while True:
    a, b, c = map(int, input().split())
    
    if a == -1 and b == -1 and c == -1:
        break
    
    if a <= 0 or b <= 0 or c <= 0:
        result.append([a, b, c, 1])
    elif a > 20 or b > 20 or c > 20:
        result.append([a, b, c, DP[20][20][20]])
    else:
        result.append([a, b, c, DP[a][b][c]])
        
for i in result:
    print("w(%d, %d, %d) = %d" %(i[0], i[1], i[2], i[3]))