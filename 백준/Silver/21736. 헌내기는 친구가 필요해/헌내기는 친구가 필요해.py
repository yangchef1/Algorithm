from collections import deque

def bfs(graph, start):
    cnt = 0
    
    need_visited = deque()
    need_visited.append(start)
    
    visited = [[False]*m for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while need_visited:
        x, y = need_visited.popleft()
        
        if graph[x][y] == "P":
            cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < n and ny < m and nx >= 0 and ny >= 0 and not visited[nx][ny] and graph[nx][ny] != 'X':
                need_visited.append((nx, ny))
                visited[nx][ny] = True
    
    if cnt == 0:
        return "TT"     
    return cnt
            
n, m = map(int, input().split())

graph = []

start = (0, 0)

for _ in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            start = (i, j)

print(bfs(graph, start))