import sys
from collections import deque

n = int(sys.stdin.readline())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = []
visited = [[0]*(n) for _ in range(n)]

for _ in range(n):
    graph.append(list(map(str, sys.stdin.readline())))


def bfs (a,b):
    need_visited = deque()
    need_visited.append((a,b))

    while need_visited:
        x, y = need_visited.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                pass
            else:
                if visited[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                    visited[nx][ny] = 1
                    need_visited.append((nx,ny))


cnt1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[0]*(n+1) for _ in range(n+1)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            cnt2 += 1

print(cnt1,cnt2)