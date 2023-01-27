t = int(input())
result = []

for i in range(t):
    n = int(input())
    DP = [0] * n
    if n == 1 or n == 2 or n == 3:
        result.append(1)
    elif n == 4 or n == 5:
        result.append(2)
    else:
        DP[0], DP[1], DP[2], DP[3], DP[4] = 1, 1, 1, 2, 2
        
        for j in range(5, n):
            DP[j] = DP[j-1] + DP[j-5]
            
        result.append(DP[n-1])

for i in result:
    print(i)