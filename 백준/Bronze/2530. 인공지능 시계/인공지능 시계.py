h, m, s = map(int, input().split())
dt = int(input())
dt += (h*3600 + m*60 + s)

a = dt // 3600
dt = dt % 3600

b = dt // 60
c = dt % 60

print(a if a < 24 else a%24, b, c)