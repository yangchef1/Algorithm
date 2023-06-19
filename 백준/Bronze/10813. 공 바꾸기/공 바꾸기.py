n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(i+1)

for i in range(m):
    a, b= map(int, input().split())
    
    temp = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = temp
        
print(*arr)