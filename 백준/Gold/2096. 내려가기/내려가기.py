import sys

n = int(sys.stdin.readline())
graph = []

max_DP = []
min_DP = []
    
for i in list(map(int, sys.stdin.readline().split())):
    max_DP.append(i)
    min_DP.append(i)

for i in range(1, n):
    a, b, c = map(int, sys.stdin.readline().split())
    min_a, min_b, min_c = min_DP[0], min_DP[1], min_DP[2]
    max_a, max_b, max_c = max_DP[0], max_DP[1], max_DP[2]
    
    min_DP[0] = min(min_a, min_b) + a 
    min_DP[1] = min(min_a, min_b, min_c) + b
    min_DP[2] = min(min_b, min_c) + c
    max_DP[0] = max(max_a,max_b) + a
    max_DP[1] = max(max_a,max_b, max_c) + b
    max_DP[2] = max(max_b,max_c) + c
    
print(max(max_DP), min(min_DP))