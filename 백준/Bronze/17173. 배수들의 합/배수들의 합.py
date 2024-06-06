n, m = map(int, input().split())
result = 0
k = list(map(int, input().split()))

for i in range(1, n + 1):
    for j in range(m):
        if i % k[j] == 0:
            result += i
            break

print(result)