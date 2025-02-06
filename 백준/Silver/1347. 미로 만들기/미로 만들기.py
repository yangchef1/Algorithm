n = int(input())
log = input()

pos = [0, 0]
path = [[0, 0]]

d = 0
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for l in log:
  if l == "F":
    pos[0] += dx[d]
    pos[1] += dy[d]
    path.append([pos[0], pos[1]])
  elif l == "R":
    d = (d + 1) % 4
  elif l == "L":
    d = (d - 1) % 4

path_x = [p[0] for p in path]
path_y = [p[1] for p in path]

x = max(path_x) - min(path_x)
y = max(path_y) - min(path_y)

board = [["#" for _ in range(x + 1)] for _ in range(y + 1)]

for px, py in path:
  board[py - min(path_y)][px - min(path_x)] = "."

for b in board:
  print("".join(b))