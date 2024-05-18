from collections import deque

def bfs():
    need_visited = deque([(1, 1)])
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    graph[1][1] = 1
    visited[1][1] = True
    ans = 1
    
    while need_visited:
        x, y = need_visited.popleft()
        
        if graph[x][y] == 0:
            continue
        
        if (x, y) in light.keys():
            for a, b in light[(x, y)]:
                if graph[a][b] == 0:
                    graph[a][b] = 1
                    for i in range(4):
                        na, nb = a + dx[i], b + dy[i]
                        if na <= n and nb <= n and na > 0 and nb > 0 and visited[na][nb]:
                            need_visited.appendleft((a, b))
                            break
                    ans += 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx <= n and ny <= n and nx > 0 and ny > 0 and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    need_visited.appendleft((nx, ny)) 
                else:
                    need_visited.append((nx, ny))
    return ans     

n, m = map(int, input().split())
light = {}

for _ in range(m):
    x, y, a, b = map(int, input().split())
    if (x, y) not in light.keys():
        light[(x, y)] = [(a, b)]  
    else:
        light[(x, y)] += [(a, b)]
    
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(bfs())