from collections import deque

n = int(input())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    graph.append(list(map(int, input().split())))

m = max(map(max, graph))

def bfs(a, b):  
    
    need_visited = deque()

    need_visited.append((a,b))
    visited[a][b] = True

    while need_visited:
        x, y = need_visited.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < n and nx >= 0 and ny < n and ny >= 0 and not visited[nx][ny] :
                visited[nx][ny] = True            
                need_visited.append((nx, ny))
                   
result = []            

for k in range(1, m + 1):  
    visited = [[False] *n for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] < k:
                visited[i][j] = True

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                bfs(i, j)
                count += 1
    
    result.append(count)
      
print(max(result))