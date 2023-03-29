from collections import deque

t = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]    

result = []

for _ in range(t):
    l = int(input())
    x, y = map(int, input().split())
    des_x, des_y = map(int, input().split())
    
    dis = [[0] *(l+1) for _ in range(l+1)]
    
    need_visited = deque()
    visited = [[False] *l for _ in range(l)]
    
    need_visited.append((x, y))
    
    while need_visited:
        a, b = need_visited.popleft()
        
        if a == des_x and b == des_y:
            break
        
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < l and ny < l and not visited[nx][ny]:   
                visited[nx][ny] = True
                need_visited.append((nx, ny))
                dis[nx][ny] = dis[a][b] + 1
                
    result.append(dis[des_x][des_y])

for i in result:
    print(i) 