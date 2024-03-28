from collections import deque

def bfs(graph, visited, start):
    need_visited = deque([start])
    visited[start[0]][start[1]] = True
    cnt = 0
    
    while need_visited:
        x, y = need_visited.popleft()
        cnt += 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < n and ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                need_visited.append((nx, ny))
                visited[nx][ny] = True
    return cnt
        

n, m = map(int, input().split())
graph = []
visited = [[False]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
width = 0
cnt = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))
   
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            width = max(width, bfs(graph, visited, (i, j)))
            cnt += 1
            
print(cnt)
print(width)