from collections import deque
import sys

def bfs(stud, visited, start):
    need_visited = deque([start])
    visited[start] = True
    path = {}
    cnt = 0
    
    while need_visited:
        node = need_visited.popleft()
        
        next_node = stud[node]
        
        path[node] = cnt
        cnt += 1

        if next_node in path.keys():
            return cnt - path[next_node]
        
        if not visited[next_node]:
            need_visited.append(next_node)
            visited[next_node] = True
    
    return 0

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    stud = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    visited = [False] * (n + 1)    
    ans = n
    
    for i in range(1, n + 1):
        if not visited[i]:
            ans -= bfs(stud, visited, i)
            
    print(ans)