from collections import deque

def bfs(x, y, graph, dis):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    need_visited = deque()
    need_visited.append((0,0))
    
    while need_visited:
        a, b = need_visited.popleft()
        if graph[a][b] == 1:
            graph[a][b] = 0
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= x or ny >= y:
                pass
            else:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    dis[nx][ny] = dis[a][b] + 1
                    need_visited.append((nx, ny))

def solution(maps):
    x, y = len(maps), len(maps[0])
    dis = [[-1]*y for _ in range(x)]
    dis[0][0] = 1    
    bfs(x, y, maps, dis)
    return dis[x-1][y-1]