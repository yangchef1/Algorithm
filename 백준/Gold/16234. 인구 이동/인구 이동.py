from collections import deque

def bfs(sx, sy):  
  union = [(sx, sy)]
  need_visited = deque([(sx, sy)])
  
  while need_visited:
    x, y = need_visited.popleft()
    
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      
      if nx < n and nx >= 0 and ny < n and ny >= 0 and not visited[nx][ny]:
        diff = abs(lands[x][y] - lands[nx][ny])
        if diff >= l and diff <= r:
          visited[nx][ny] = True
          need_visited.append((nx, ny))
          union.append((nx, ny))
  
  return union
    
        
n, l, r = map(int, input().split())
lands = [list(map(int, input().split())) for _ in range(n)]

day = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while True:  
  f = lands[0][0]
  if all(cell == f for row in lands for cell in row):
    break
  
  unions = []
  visited = [[False] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        visited[i][j] = True
        unions.append(bfs(i, j))
        
  if all([len(u) == 1 for u in unions]):
    break
  
  for union in unions:
    v = sum([lands[x][y] for x, y in union]) // len(union)
    for x, y in union:
      lands[x][y] = v
  
  day += 1  
  
print(day)