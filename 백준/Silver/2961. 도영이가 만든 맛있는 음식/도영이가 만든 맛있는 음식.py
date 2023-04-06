def backtracking(m, start):
    
    global result
    
    if len(ans) == m:
        S, B = 1, 0
        for i in ans:
            S *= i[0]
            B += i[1]
        if absolute(S, B) < result:
            result = absolute(S, B)
        return
    
    for i in range(start, n):
        if i not in ans:
            ans.append(ingrediant[i])
            backtracking(m, i+1)
            ans.pop()


def absolute(a, b):
    if a - b < 0:
        return b - a
    else:
        return a - b
    

n = int(input())

ingrediant = []

for i in range(n):
    ingrediant.append(list(map(int, input().split())))
      
ans = []
result = 1000000000

for i in range(1, n+1):
    backtracking(i, 0)
    
print(result)