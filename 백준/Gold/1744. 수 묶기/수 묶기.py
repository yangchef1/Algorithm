n = int(input())

p = []
m = []
z_count = 0
o_count = 0

for _ in range(n):
  num = int(input())
  if num < 0:
    m.append(num)
  elif num == 0:
    z_count += 1
  elif num == 1:
    o_count += 1
  else:
    p.append(num)
  
p.sort(reverse=True)
m.sort()

sum = 0

for i in range(0, len(p) - 1, 2):
  sum += (p[i] * p[i + 1])

for i in range(0, len(m) - 1, 2):
  sum += (m[i] * m[i + 1])
  
sum += o_count

if len(m) % 2 == 1 and z_count == 0:
  sum += m[-1]

if len(p) % 2 == 1:
  sum += p[-1]
  
print(sum)