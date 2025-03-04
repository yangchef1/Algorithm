import math

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

result = 0

for s in size:
  result += math.ceil(s / t)

print(result)
print(n // p, n % p)