from collections import deque

def bfs(graph):
    need_visited = deque([(0, 0, 0)])
    dis = [[[0, 0] for _ in range(m) ] for _ in range(n)] # bw : 0 -> 아직 벽이 부서진 적 없는 세계, bw : 1 -> 벽이 한번 부서진 세계
    dis[0][0][0] = 1
    
    while need_visited:
        x, y, bw = need_visited.popleft()
        
        if x == n - 1 and y == m - 1:
            return dis[x][y][bw]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
           
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] == 0 and dis[nx][ny][bw] == 0: # 다음 경로 == 길 and 다음 경로 == 미방문 노드
                    dis[nx][ny][bw] = dis[x][y][bw] + 1
                    need_visited.append((nx, ny, bw))
                if graph[nx][ny] == 1 and bw == 0: # 다음 경로 == 벽 and 현재 세계 == 벽이 부서지지 않은 세계
                    dis[nx][ny][1] = dis[x][y][0] + 1
                    need_visited.append((nx, ny, 1))                
    return -1

n, m = map(int, input().split())    
graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    graph.append(list(map(int, input())))

print(bfs(graph))    