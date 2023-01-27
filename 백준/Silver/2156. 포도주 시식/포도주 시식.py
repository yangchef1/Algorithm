n = int(input())
k = []

for i in range(n):
    k.append(int(input()))
    
DP = [0] * n

if n == 1:
    print(k[0])
elif n == 2:
    print(k[0]+k[1])
elif n == 3:
    print(max(k[0]+k[1], k[0]+k[2], k[1]+k[2]))
else:
    DP[0] = k[0]
    DP[1] = k[0] + k[1]
    DP[2] = max(k[0]+k[1], k[0]+k[2], k[1]+k[2])
    
    for i in range(3,n):
        DP[i] = max(DP[i-3]+k[i-1]+k[i], DP[i-2]+k[i], DP[i-1])
        
    print(DP[n-1])