arr = [0] * 30

for i in range(28):
    n = int(input())
    
    arr[n-1] = 1
    
print(arr.index(0)+1)
arr[arr.index(0)] = 1
print(arr.index(0)+1)