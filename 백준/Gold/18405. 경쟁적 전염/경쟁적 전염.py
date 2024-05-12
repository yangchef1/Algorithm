from collections import deque

def bfs(graph, virus, visited):
    need_visited = deque(virus)
    
    while need_visited:
        v, x, y, t = need_visited.popleft()
        
        if t == s + 1:
            break
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < n and ny < n and nx >= 0 and ny >= 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = v
                need_visited.append((v, nx, ny, t + 1))
                
    return graph[X - 1][Y - 1]

n, k = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split()))) 

visited = [[False] * n for _ in range(n)]
virus = []

for i in range(n):
    for j in range(n):
        v = graph[i][j]
        if v != 0:
            visited[i][j] = True
            virus.append((v, i, j, 1))
            
virus.sort(key = lambda x : x[0])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

s, X, Y = map(int, input().split())

print(bfs(graph, virus, visited))