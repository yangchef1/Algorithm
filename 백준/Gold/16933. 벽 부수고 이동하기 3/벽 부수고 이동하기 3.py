from collections import deque
import sys

def bfs():
    need_visited = deque([(0, 0, 0, 1)]) # 낮 == odd / 밤 == even
    visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
    visited[0][0][0] = 1
    ans = float('inf')
    
    while need_visited:
        x, y, bw, dn = need_visited.popleft()
    
        if x == n - 1 and y == m - 1:
            ans = min(ans, visited[bw][x][y])
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                next_node = graph[nx][ny]
                if dn % 2 == 1 and next_node == 1 and bw < k and visited[bw + 1][nx][ny] == 0:
                    visited[bw + 1][nx][ny] = dn + 1
                    need_visited.append((nx, ny, bw + 1, dn + 1))
                if dn % 2 == 0 and next_node == 1 and bw < k and visited[bw + 1][nx][ny] == 0:
                    need_visited.append((x, y, bw, dn + 1))
                if next_node == 0 and visited[bw][nx][ny] == 0:
                    visited[bw][nx][ny] = dn + 1
                    need_visited.append((nx, ny, bw, dn + 1))
    return -1 if ans == float('inf') else ans
            
n, m, k = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
    
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
    
print(bfs())