import sys

n, m = map(int, input().split())
arr = []

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    
    for i in range(1, m):
        temp[i] += temp[i - 1]
    
    arr.append(temp)

k = int(input())

for _ in range(k):
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
    sum = 0
    
    for i in range(a - 1, c):
        sum += (arr[i][d - 1] - (arr[i][b - 2]  if b >= 2 else 0))
    
    print(sum)