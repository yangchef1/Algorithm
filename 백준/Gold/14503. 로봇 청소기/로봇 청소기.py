n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]    

cnt = 0

while True:
    
    if graph[x][y] == 0:
        graph[x][y] = 2
        cnt += 1
        
    is_cleaned = True
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and ny >= 0 and nx < n and ny < m and graph[nx][ny] == 0:
            is_cleaned = False
            
    if not is_cleaned:
        d = d-1 if d != 0 else 3
        
        if x + dx[d] >= 0 and y + dy[d] >= 0 and x + dx[d] < n and y + dy[d] < m and graph[x + dx[d]][y + dy[d]] == 0:
            x += dx[d]
            y += dy[d]
    
    if is_cleaned:
        if x-dx[d] < 0 or y-dy[d] < 0 or x-dx[d] >= n or y-dy[d] >=m or graph[x-dx[d]][y-dy[d]] == 1:
            break
        else:
            x -= dx[d]
            y -= dy[d]
    
print(cnt)