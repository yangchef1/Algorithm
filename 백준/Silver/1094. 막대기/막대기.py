x = int(input())
result = 0

for i in range(6, -1, -1):
    if x >= 2 ** i:
        result += 1
        x -= 2 ** i
    
    if x == 0:
        break
    
print(result)