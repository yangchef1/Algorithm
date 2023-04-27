def Backtracking(i, col):
    
    global result

    if i == n :
            result += 1
            return
    
    for j in range(n):
        col[i] = j
        if promising(i, col):
            Backtracking(i+1, col)
        
def promising(i, col):
    for k in range(i):
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            return False
        
    return True

n = int(input())
col = [0] * n
result = 0
Backtracking(0, col)

print(result)