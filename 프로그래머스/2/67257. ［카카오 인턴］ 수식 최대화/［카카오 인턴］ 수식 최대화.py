from itertools import permutations

def cal(a, b, op):
    if op == "*":
        return a * b
    if op == "+":
        return a + b
    if op == "-":
        return a - b

def solution(expression):
    l = len(expression)
    exp = []
    ops = []
    if "*" in expression:
        ops.append("*")
    if "+" in expression:
        ops.append("+")
    if "-" in expression:
        ops.append("-")
    
    
    last_op = 0
    for i in range(l):
        if expression[i] in ops:
            exp.append(int(expression[last_op: i]))
            exp.append(expression[i])
            last_op = i + 1
    exp.append(int(expression[last_op:]))
    
    prioritys = permutations(ops)
    answer = 0
    
    for pri in prioritys:
        temp_exp = list(map(lambda x:x, exp))
        for p in pri:
            i = 0
            le = len(temp_exp)
            while le != 1 and i < len(temp_exp) - 1:
                if temp_exp[i] == p:
                    temp_exp[i] = cal(temp_exp[i - 1], temp_exp[i + 1], p)
                    del temp_exp[i - 1]
                    del temp_exp[i]
                else:
                    i += 1
        result = abs(temp_exp[0])
        if answer < result:
            answer = result
        print(result, pri)
    
    return answer