from collections import deque

s = input()

sum = 0
LEN = len(s)
cnt = 0

need_visited = deque()
need_visited.append([1, 0])

while need_visited:
    
    node, idx = need_visited.popleft()
    
    if idx == LEN:
        sum += node
    else:
        if s[idx] == 'L':
            need_visited.append((2*node, idx+1))
        elif s[idx] == 'R':
            need_visited.append((2*node+3**(cnt), idx+1))
        elif s[idx] == 'P':
            need_visited.append((node, idx+1))
        else:
            # need_visited.append((2*node, idx+1))
            # need_visited.append((2*node+1, idx+1))
            # need_visited.append((node, idx+1))
            need_visited.append((5*node + 3**(cnt), idx + 1))
            cnt += 1

print(sum)