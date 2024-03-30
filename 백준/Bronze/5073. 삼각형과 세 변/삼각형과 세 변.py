result = []

while True:
    l = list(map(int, input().split()))
    
    if l[0] == 0 and l[1] == 0 and l[2] == 0:
        break
    
    l.sort()
    
    if l[0] + l[1] > l[2]:
        if l[0] == l[1] and l[1] == l[2]:
            result.append("Equilateral")
        elif l[0] != l[1] and l[1] != l[2] and l[2] != l[0]:
            result.append("Scalene")
        else:
            result.append("Isosceles")    
    else:
        result.append("Invalid")
        
print("\n".join(map(str, result)))