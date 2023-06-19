n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(i+1)

for i in range(m):
    a, b= map(int, input().split())
    
    arr = arr[:a-1] + list(reversed(arr[a-1:b])) + arr[b:]
        
print(*arr)