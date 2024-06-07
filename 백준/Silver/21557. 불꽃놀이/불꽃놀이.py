n = int(input())
fire = list(map(int, input().split()))

k = abs(fire[-1] - fire[0])
    
if n - 2 < k:
    print(max(fire[-1], fire[0]) - (n - 2))
else:
    print(min(fire[-1], fire[0]) - ((n - 1 - k) // 2))