from collections import deque

def bfs(graph, visited, dis, start, dest):
    need_visited = deque([start])
    
    while need_visited:
        x, y, z = need_visited.popleft()
        
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            
            if nx >= 0 and ny >= 0 and nz >= 0 and nx < n and ny < m and nz < l and not visited[nz][nx][ny] and graph[nz][nx][ny] != "#":
                visited[nz][nx][ny] = True
                need_visited.append((nx, ny, nz))
                dis[nz][nx][ny] = dis[z][x][y] + 1

    a, b, c = dest
    return dis[c][a][b]
        
        

result = []

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
    
    l, n, m = map(int, input().split())

    if l == 0 and n == 0 and m == 0:
        break
    
    building = [[]for _ in range(l)]
    visited = [[[False]*m for _ in range(n)]for _ in range(l)]
    dis = [[[0]*m for _ in range(n)]for _ in range(l)]
    
    for i in range(l):
        for j in range(n):
            building[i].append(list(input()))
        input()
    
    start = ()
    dest = ()        
        
    for i in range(l):
        for j in range(n):
            for k in range(m):
                if building[i][j][k] == "S":
                    start = (j, k, i)
                if building[i][j][k] == "E":
                    dest = (j, k, i)
   
    ans = bfs(building, visited, dis, start, dest)        
            
    result.append("Escaped in {0} minute(s).".format(ans) if ans != 0 else "Trapped!")
    
print("\n".join(result))
