n = int(input())
arr = list(map(int, input().split()))

DP = [1] * n
result = []

for i in range(n):
    result.append([arr[i]])
    
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and DP[i] < DP[j] + 1:
                DP[i] = DP[j] + 1
                result[i] = result[j] + [arr[i]]

m = DP.index(max(DP))
print(DP[m])
print(*result[m])