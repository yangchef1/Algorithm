n = int(input())
card = [0]
card.extend(list(map(int, input().split())))

DP = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i, n+1):
        DP[j] = max(DP[j], DP[j-i] + card[i])
        
print(DP[n])