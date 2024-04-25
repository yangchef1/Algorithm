n = int(input())
house = []
cost = [[0] * n for _ in range(3)] # 0 - R / 1 - G / 2 - B
ans = float('inf')

for _ in range(n):
    house.append(list(map(int, input().split())))

for i in range(3):
    cost[i][0], cost[i - 1][0], cost[i - 2][0] = house[0][i], float('inf'), float('inf')
    
    for j in range(1, n):
        cost[0][j] = min(cost[1][j - 1], cost[2][j - 1]) + house[j][0]
        cost[1][j] = min(cost[0][j - 1], cost[2][j - 1]) + house[j][1]
        cost[2][j] = min(cost[1][j - 1], cost[0][j - 1]) + house[j][2]
    
    ans = min(ans, cost[i - 1][-1], cost[i - 2][-1])

print(ans)