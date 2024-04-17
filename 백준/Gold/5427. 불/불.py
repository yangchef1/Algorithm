from collections import deque
import sys

def bfs(graph, start):
    need_visited = deque([start])
    visited = [[False] * n for _ in range(m)]
    visited[start[0]][start[1]] = True
    stars = []
    level = 0
    
    for i in range(m):
        for j in range(n):
            if graph[i][j] == '*':
                stars.append((i, j))
                visited[i][j] = True
    
    while need_visited:
        x, y, d = need_visited.popleft()
           
        if d > level:
            temp = []                   
            for a, b in stars:
                for i in range(4):
                    na, nb = a + dx[i], b + dy[i]
                    if na >= 0 and nb >= 0 and na < m and nb < n and graph[na][nb] != '*' and graph[na][nb] != '#':
                        graph[na][nb] = '*'
                        visited[na][nb] = True
                        temp.append((na, nb))
            stars = temp  
            
        if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and graph[x][y] != '*':
            return d + 1
                                            
        level = d
        
        for i in range(4):
            nx, ny= x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx < m and ny < n and not visited[nx][ny] and graph[nx][ny] == '.':
                visited[nx][ny] = True
                need_visited.append((nx, ny, d + 1))  
                
    return 'IMPOSSIBLE'  

t = int(sys.stdin.readline().rstrip())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = []

for i in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    start = 0
    
    for j in range(m):
        graph.append(list(sys.stdin.readline().rstrip()))
        if '@' in graph[-1]:
            start = (j, graph[-1].index('@'), 0)
            
    result.append(bfs(graph, start))

print("\n".join(map(str, result)))