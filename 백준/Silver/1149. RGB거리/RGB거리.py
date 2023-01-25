n = int(input())

house = []

R = [-1] * n
G = [-1] * n
B = [-1] * n

for i in range(n):
    house.append(list(map(int, input().split())))
    
R[0], G[0], B[0] = house[0][0], house[0][1], house[0][2]

for i in range(1,n):
    R[i] = min(G[i-1],B[i-1]) + house[i][0]
    G[i] = min(R[i-1],B[i-1] )+ house[i][1]
    B[i] = min(G[i-1],R[i-1]) + house[i][2]
    
print(min(R[n-1], G[n-1], B[n-1])) 