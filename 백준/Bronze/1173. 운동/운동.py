N, m, M, T, R = map(int, input().split())
p = m
result = 0

while N != 0:
  if p + T <= M:
    p += T
    N -= 1
  elif p > m:
    if p - R >= m:
      p -= R  
    else:
      p = m
  else:
    print(-1)
    exit(0)
  
  result += 1
  
print(result)