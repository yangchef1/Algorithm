from collections import deque
import sys

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(sx, sy):
  size = 2
  eaten = 0
  time = 0
  
  while True:
    need_visited = deque([[0, sx, sy]])
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True
    fishes = []

    while need_visited:
      dis, x, y = need_visited.popleft()

      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < n and nx >= 0 and ny < n and ny >= 0 and not visited[nx][ny] and size >= board[nx][ny]:
          pos = board[nx][ny]
          if pos < 7 and pos > 0 and size > pos:
            fishes.append([dis + 1, nx, ny])
          visited[nx][ny] = True
          need_visited.append([dis + 1, nx, ny])

    if not fishes:
      return time
    
    fishes.sort(key = lambda x: (x[0], x[1], x[2]))
    
    board[sx][sy] = 0
    
    dis, sx, sy = fishes[0]
    board[sx][sy] = 9
    
    time += dis
    eaten += 1

    if eaten == size:
      size += 1
      eaten = 0

n = int(input())

board = []
shark_x, shark_y = 0, 0

for i in range(n):
  a = list(map(int, sys.stdin.readline().strip().split()))
  board.append(a)
  if 9 in a:
    shark_x, shark_y = i, a.index(9)
    
print(bfs(shark_x, shark_y))