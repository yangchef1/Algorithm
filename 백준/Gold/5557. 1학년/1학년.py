n = int(input())
number = list(map(int, input().split()))

DP = [[0]*21 for _ in range(n-1)]
DP[0][number[0]] = 1

for i in range(1, n-1):    
    for j in range(21):
        if DP[i-1][j] != 0:
            plus, minus = j + number[i], j - number[i]
            
            if plus >= 0 and plus <= 20:
                DP[i][plus] += DP[i-1][j]

            if minus >= 0 and minus <= 20:
                DP[i][minus] += DP[i-1][j]
    
print(DP[-1][number[-1]])