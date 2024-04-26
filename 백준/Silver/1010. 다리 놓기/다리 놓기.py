from math import comb

t = int(input())
result = []

for _ in range(t):
    n, m = map(int, input().split())
    result.append(comb(m, n))

print("\n".join(map(str, result)))