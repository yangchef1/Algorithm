n = int(input())
wire = []
DP = [1] * n

for i in range(n):
    wire.append(list(map(int, input().split())))
    
wire.sort(key = lambda x : x[0])
    
for i in range(n):
    for j in range(i):
        if wire[i][0] > wire[j][0] and wire[i][1] > wire[j][1]:
            DP[i] = max(DP[i], DP[j] + 1)
            
print(n - max(DP))