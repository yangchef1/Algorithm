def Backtracking(i, oper):
    
    global value
    
    if i == n-1:
        result.append(value[-1])
        return

    for j in range(4):        
        if oper[j] != 0:
            oper[j] -= 1
            if j == 0:
                value.append(value[-1] + number[i+1])
                Backtracking(i+1, oper)
            elif j == 1:
                value.append(value[-1] - number[i+1])
                Backtracking(i+1, oper)
            elif j == 2:
                value.append(value[-1] * number[i+1])
                Backtracking(i+1, oper)
            else:
                value.append(int(value[-1] / number[i+1]))
                Backtracking(i+1, oper)
            oper[j] += 1
            value.pop()
                        

            


n = int(input())
number = list(map(int, input().split()))
operator = list(map(int, input().split()))
value = []
value.append(number[0])
result = []

Backtracking(0, operator)

print(max(result))
print(min(result))