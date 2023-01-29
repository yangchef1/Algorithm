n = int(input())
arr = list(map(int, input().split()))

LDS = [1] * n
          
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            LDS[i] = max(LDS[i], LDS[j] + 1)
    
print(max(LDS))