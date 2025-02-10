n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for command in commands:
  nx, ny = x + dx[command - 1], y + dy[command - 1]
  
  if nx >= n or nx < 0 or ny >= m or ny < 0:
    continue
  
  if command == 1:
    dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
  elif command == 2:
    dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
  elif command == 3:
    dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
  else:
    dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    
  if board[nx][ny] == 0:
    board[nx][ny] = dice[5]
  else:
    dice[5] = board[nx][ny]
    board[nx][ny] = 0

  print(dice[0])
  
  x, y = nx, ny