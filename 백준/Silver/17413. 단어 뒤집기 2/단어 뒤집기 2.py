from collections import deque

s = input()
result = ""
is_tag = False
stack = deque()

for i in range(len(s)):    
    if s[i] == "<":
        is_tag = True
        for _ in range(len(stack)):
            result += stack.pop()
            
    stack.append(s[i])
    
    if s[i] == ">":
        is_tag = False
        for _ in range(len(stack)):
            result += stack.popleft()
            
    if not is_tag and s[i] == " ":
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += " "    

for _ in range(len(stack)):
    result += stack.pop()

print(result)