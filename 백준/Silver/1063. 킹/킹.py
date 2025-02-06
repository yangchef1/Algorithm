k, r, n = input().split()
king = [ord(k[0]) - 64, int(k[1])]
rock = [ord(r[0]) - 64, int(r[1])]
n = int(n)

move = {"R" : [1, 0], "L" : [-1, 0], "T" : [0, 1], "B" : [0, -1], "RT" : [1, 1], "LT" : [-1, 1], "RB" : [1, -1], "LB" : [-1, -1]}

for i in range(n):
  dx, dy = move[input()]
  
  if king[0] + dx > 8 or king[0] + dx < 1 or king[1] + dy > 8 or king[1] + dy < 1:
    continue
  
  if (king[0] + dx == rock[0] and king[1] + dy == rock[1]) and (rock[0] + dx > 8 or rock[0] + dx < 1 or rock[1] + dy > 8 or rock[1] + dy < 1):
    continue
  
  king[0] += dx
  king[1] += dy
  
  if king[0] == rock[0] and king[1] == rock[1]:
    rock[0] += dx
    rock[1] += dy
    
print(chr(king[0] + 64) + str(king[1]))
print(chr(rock[0] + 64) + str(rock[1]))