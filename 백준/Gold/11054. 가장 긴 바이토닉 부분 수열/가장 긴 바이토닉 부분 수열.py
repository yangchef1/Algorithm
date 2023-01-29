n = int(input())
arr = list(map(int, input().split()))

LIS = [1] * n
LDS = [1] * n
BI = [0] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            LIS[i] = max(LIS[i], LIS[j] + 1)
            
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            LDS[i] = max(LDS[i], LDS[j] + 1)
            
for i in range(n):
    BI[i] = LIS[i] + LDS[i]
    
print(max(BI)-1)