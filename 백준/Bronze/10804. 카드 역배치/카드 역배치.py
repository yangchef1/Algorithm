li = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    temp = li[a - 1: b][::-1]
    
    for i in range(b - a + 1):
        li[a + i - 1] = temp[i]
    
print(" ".join(map(str, li)))  