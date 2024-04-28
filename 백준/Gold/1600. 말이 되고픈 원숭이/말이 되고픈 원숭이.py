from collections import deque

def bfs():
    need_visited = deque([(0, 0, 0)])
    visited = [[[0] * (k + 1) for _ in range(n)] for _ in range(m)]
    visited[0][0][0] = 0
    
    while need_visited:
        x, y, h = need_visited.popleft()

        if x == m - 1 and y == n - 1:
            return visited[x][y][h]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < m and ny < n and visited[nx][ny][h] == 0 and graph[nx][ny] == 0:
                visited[nx][ny][h] = visited[x][y][h] + 1
                need_visited.append((nx, ny, h))
                
        for i in range(8):
            hnx, hny = x + horse_dx[i], y + horse_dy[i]
            
            if hnx >= 0 and hny >= 0 and hnx < m and hny < n and h < k and visited[hnx][hny][h + 1] == 0 and graph[hnx][hny] == 0:
                visited[hnx][hny][h + 1] = visited[x][y][h] + 1
                need_visited.append((hnx, hny, h + 1))
                
        
    return -1
    

k = int(input())
n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
horse_dx = [2, 2, -2, -2, 1, 1, -1, -1]   
horse_dy = [1, -1, 1, -1, 2, -2, 2, -2]
graph = []

for i in range(m):
    graph.append(list(map(int, input().split())))
    
print(bfs())