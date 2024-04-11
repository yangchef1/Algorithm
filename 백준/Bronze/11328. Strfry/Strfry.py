def isPossible(a, b):
    if len(a) != len(b):
        return "Impossible"
    
    for i in a:
        if i not in b:
            return "Impossible"
        if i in b:
            b.remove(i)
    
    return "Possible"
    
n = int(input())

result = []

for i in range(n):
    a, b = map(list, input().split())
    result.append(isPossible(a, b))
    
print("\n".join(map(str, result)))