import sys
from collections import deque

x, y = map(int,sys.stdin.readline().split())

graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(x):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dis = [[0]*y for _ in range(x)]

need_visited = deque()

n = 0
dis[0][0] = 1
need_visited.append((0,0))

while need_visited:
    a, b = need_visited.popleft()
    if graph[a][b] == 1:
        graph[a][b] = 0
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx < 0 or ny < 0 or nx >= x or ny >= y:
            pass
        else:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dis[nx][ny] = dis[a][b] + 1
                need_visited.append((nx, ny))

print(dis[x-1][y-1])