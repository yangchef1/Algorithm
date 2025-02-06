gear = []
for _ in range(4):
  gear.append(list(map(int, list(input()))))

def rotate(m, d, need_rotate):  
  if d == 1:
    l = gear[m].pop()
    gear[m].insert(0, l)
  else:
    f = gear[m].pop(0)
    gear[m].append(f)
    
  visited[m] = True
    
  if m < 3 and not visited[m + 1] and need_rotate[m]:
    rotate(m + 1, -d, need_rotate)
  
  if m > 0 and not visited[m - 1] and need_rotate[m - 1]:
    rotate(m - 1, -d, need_rotate)

n = int(input())

for i in range(n):
  m, d = map(int, input().split())
  
  visited = [False for _ in range(4)]
  
  need_rotate = []
  for i in range(3):
    need_rotate.append(gear[i][2] != gear[i + 1][6])
  
  rotate(m - 1, d, need_rotate)
      
score = 0
for i in range(4):
  if gear[i][0] == 1:
    score += (2**i)
  
print(score)