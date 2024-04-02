import sys
from collections import deque

deq = deque()
result = []
n = int(input())

for i in range(n):
    k = sys.stdin.readline().rstrip().split()
    
    if k[0] == '1':
        deq.appendleft(k[1])
    elif k[0] == '2':
        deq.append(k[1])
    elif k[0] == '3':
        result.append(deq.popleft() if deq else -1)
    elif k[0] == '4':
        result.append(deq.pop() if deq else -1)
    elif k[0] == '5':
        result.append(len(deq))
    elif k[0] == '6':
        result.append(0 if deq else 1)
    elif k[0] == '7':
        result.append(deq[0] if deq else -1)
    else:
        result.append(deq[-1] if deq else -1)
        
print("\n".join(map(str, result)))