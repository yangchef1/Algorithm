from collections import deque

def bfs(graph, start):
    need_visited = deque([start])
    visited = [[False] * c for _ in range(r)]
    visited[start[0]][start[1]] = True
    stars = []
    level = 0
    
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'F':
                stars.append((i, j))
                visited[i][j] = True
    
    while need_visited:
        x, y, d = need_visited.popleft()
           
        if d > level:
            temp = []                   
            for a, b in stars:
                for i in range(4):
                    na, nb = a + dx[i], b + dy[i]
                    if na >= 0 and nb >= 0 and na < r and nb < c and graph[na][nb] != 'F' and graph[na][nb] != '#':
                        graph[na][nb] = 'F'
                        visited[na][nb] = True
                        temp.append((na, nb))
            stars = temp  
            
        if (x == 0 or x == r - 1 or y == 0 or y == c - 1) and graph[x][y] != 'F':
            return d + 1
                                            
        level = d
        
        for i in range(4):
            nx, ny= x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx < r and ny < c and not visited[nx][ny] and graph[nx][ny] == '.':
                visited[nx][ny] = True
                need_visited.append((nx, ny, d + 1))  
                
    return 'IMPOSSIBLE'  

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

r, c = map(int, input().split())
graph = []
start = 0

for j in range(r):
    graph.append(list(input()))
    if 'J' in graph[-1]:
        start = (j, graph[-1].index('J'), 0)
        
print(bfs(graph, start))