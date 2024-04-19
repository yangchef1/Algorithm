from collections import deque

def bfs(graph):
    need_visited = deque([(0, 0, 0)])
    dis = [[[0] * (m) for _ in range(n)] for _ in range(k + 1)]
    dis[0][0][0] = 1
    
    while need_visited:
        bw, x, y = need_visited.popleft()
        
        if x == n - 1 and y == m - 1:
            return dis[bw][x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
           
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] == 0 and dis[bw][nx][ny] == 0:
                    dis[bw][nx][ny] = dis[bw][x][y] + 1 
                    need_visited.append((bw, nx, ny))
                if graph[nx][ny] == 1 and bw < k and dis[bw + 1][nx][ny] == 0:
                    dis[bw + 1][nx][ny] = dis[bw][x][y] + 1
                    need_visited.append((bw + 1, nx, ny))                
    return -1

n, m, k = map(int, input().split())    
graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    graph.append(list(map(int, input())))

print(bfs(graph))    