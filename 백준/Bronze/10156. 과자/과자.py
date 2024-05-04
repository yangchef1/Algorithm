k, n, m = map(int, input().split())
ans = k*n - m
print(ans if ans > 0 else 0)