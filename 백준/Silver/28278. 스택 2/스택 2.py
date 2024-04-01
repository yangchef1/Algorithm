import sys

stack = []
result = []
n = int(input())

for i in range(n):
    k = sys.stdin.readline().rstrip().split()
    
    if k[0] == '1':
        stack.append(k[1])
    elif k[0] == '2':
        result.append(stack.pop() if stack else -1)
    elif k[0] == '3':
        result.append(len(stack))
    elif k[0] == '4':
        result.append(0 if stack else 1)
    else:
        result.append(stack[-1] if stack else -1)
        
print("\n".join(map(str, result)))