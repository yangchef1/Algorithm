result = []
for _ in range(3):
    cnt = list(map(int, input().split())).count(0)
    
    if cnt == 1:
        result.append('A')
    elif cnt == 2:
        result.append('B')
    elif cnt == 3:
        result.append('C')
    elif cnt == 4:
        result.append('D')
    else:
        result.append('E')
print("\n".join(map(str, result)))