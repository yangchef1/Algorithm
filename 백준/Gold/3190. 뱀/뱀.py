from collections import deque

n = int(input())
body = deque([(0, 0)])
dir = 0
graph = [[0] * n for _ in range(n)]
varPos = {}
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

k = int(input())
for a in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
    
l = int(input())
for p in range(l):
    t, c = input().split()
    varPos[int(t)] = c

graph[0][0] = 2

for i in range(10001):
    
    # 방향 전환
    k = varPos.get(i, None)
    
    if k == "L":
        dir = (dir + 1) % 4
    elif k == "D":
        dir = (dir - 1) % 4
    
    nx, ny = body[-1][0] + dx[dir], body[-1][1] + dy[dir]
    
    body.append((nx, ny))
    
    # 게임 오버
    if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 2:
        print(i + 1)
        break
    
    # 사과 여부 분기
    if graph[nx][ny] == 0:
        a, b = body.popleft()
        graph[a][b] = 0
        
    graph[nx][ny] = 2