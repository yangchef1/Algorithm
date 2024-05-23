n = int(input())
a, b = 100, 100

for _ in range(n):
    m, n = map(int, input().split())
    
    if m > n:
        b -= m
    elif n > m:
        a -= n

print(a)
print(b)