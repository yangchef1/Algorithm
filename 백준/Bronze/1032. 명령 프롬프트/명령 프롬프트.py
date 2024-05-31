n = int(input())
dir = []
for _ in range(n):
    dir.append(input())
    
comp, result = dir[0], dir[0]
l = len(dir[0])

for i in range(1, n):
    result = ""
    for j in range(l):
        if comp[j] != dir[i][j]:
            result += "?"
        else:
            result += comp[j]
    comp = result
    
print(result)