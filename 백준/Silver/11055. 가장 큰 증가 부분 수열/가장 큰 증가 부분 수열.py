n = int(input())
arr = list(map(int, input().split()))

DP = [0] * n

for i in range(n):
    DP[i] = arr[i]    

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            DP[i] = max(DP[i], DP[j] + arr[i])
            
print(max(DP))