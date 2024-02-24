def dfs(graph, start, visited):
    result = 0
    
    need_visited = [start]
    visited[start[0]][start[1]] = True
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while need_visited:
        x, y = need_visited.pop()
        result += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                pass
            elif not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                visited[nx][ny] = True
                need_visited.append((nx, ny))
    return result
                
n, m = map(int, input().split())
maps = []
for _ in range(m):
    maps.append(list(input()))

visited = [[False]*n for _ in range(m)]
w = 0
b = 0

for i in range(len(maps)):
    for j in range(len(maps[0])):
        if not visited[i][j]:
            result = dfs(maps, (i,j), visited)
            if maps[i][j] == 'W':
                w += result ** 2
            else:
                b += result ** 2

print(w, b)