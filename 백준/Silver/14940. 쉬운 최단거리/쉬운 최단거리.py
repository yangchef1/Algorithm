from collections import deque

def bfs(graph, dis, start):    
    need_visited = deque()
    need_visited.append(start)
    
    visited = [[False]*m for _ in range(n)]
    visited[start[0]][start[1]] = True    
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while need_visited:
        x, y = need_visited.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < n and ny < m and nx >= 0 and ny >= 0 and not visited[nx][ny] and graph[nx][ny] != 0:
                need_visited.append((nx, ny))
                visited[nx][ny] = True
                dis[nx][ny] = dis[x][y] + 1
            
n, m = map(int, input().split())

graph = []
dis = [[-1]*m for _ in range(n)]

start = (0, 0)

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i, j)
            dis[i][j] = 0
        if graph[i][j] == 0:
            dis[i][j] = 0

bfs(graph, dis, start)

for i in dis:
    print(" ".join(map(str, i)))