import sys
from collections import deque

def bfs(graph, visited, start):
    need_visited = deque()
    need_visited.append(start)
    visited[start[0]][start[1]] = True
    
    while need_visited:
        x, y = need_visited.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if graph[nx][ny] != 0 and nx >= 0 and ny >= 0 and nx < n and ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                need_visited.append((nx, ny))                

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0
year = 1

while graph != [[0]*m for _ in range(n)]:
    
    next_graph = [[0]*m for _ in range(n)]
    
    for x in range(n):
        for y in range(m):
            if graph[x][y] != 0:
                sea = 0
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if graph[nx][ny] == 0 and nx >= 0 and ny >= 0 and nx < n and ny < m:
                        sea += 1
                next_graph[x][y] = graph[x][y] - sea if graph[x][y] >= sea else 0
    
    graph = next_graph
    
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] != 0:
                bfs(graph, visited, (i, j))
                cnt += 1
    
    if cnt >= 2:
        result = year
        break
    
    year += 1
    
print(result)