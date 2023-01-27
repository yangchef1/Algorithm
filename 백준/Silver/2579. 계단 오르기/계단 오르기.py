n = int(input())
step = [0]
DP = [0] * (n+1)

for i in range(n):
    step.append(int(input()))

if n == 1:
    print(step[1])
elif n == 2:
    print(step[1]+step[2])
else:
    DP[1] = step[1]
    DP[2] = step[1] + step[2]
    for i in range(3, n+1):
        DP[i] = max(DP[i-2]+step[i], DP[i-3]+step[i-1]+step[i]) 
    print(DP[n])