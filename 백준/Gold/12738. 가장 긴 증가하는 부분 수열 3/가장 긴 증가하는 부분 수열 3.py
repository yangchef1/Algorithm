import bisect

n = int(input())
arr = list(map(int, input().split()))

lis = []
ans = 0

for i in arr:
    if not lis:
        lis.append(i)
        ans += 1
        continue
    
    if lis[-1] < i:
        lis.append(i)
        ans += 1
    else:
        k = bisect.bisect_left(lis, i)
        lis[k] = i
           
print(ans)