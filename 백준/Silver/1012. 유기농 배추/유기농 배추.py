import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = []

t = int(sys.stdin.readline())


def bfs (x,y):
    need_visited = deque()
    need_visited.append((x,y))
    while need_visited:
        a, b = need_visited.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                pass
            else:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    need_visited.append((nx,ny))


for j in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0]*n for _ in range(m)]
    count = 0
    for i in range(k):
        a, b = map(int,sys.stdin.readline().split())
        graph[a][b] = 1
    for q in range(m):
        for p in range(n):
            if graph[q][p] == 1:
                bfs(q,p)
                count += 1
            else:
                pass
    result.append(count)

for i in result:
    print(i)