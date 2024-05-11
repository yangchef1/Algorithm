t = int(input())
ans = []

for _ in range(t):
    a, b, c = map(int, input().split())
    
    if a == b and b == c:
        ans.append(10000 + a*1000)
    elif a != b and b != c and c != a:
        ans.append(100*max(a, b, c))
    elif a == b or a == c:
        ans.append(1000 + 100*a)
    else:
        ans.append(1000 + 100*b)
        
print(max(ans))