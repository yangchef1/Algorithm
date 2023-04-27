from collections import deque

def bfs(start):
    need_visited = deque()
    need_visited.append(start)
    
    while need_visited:
        node = need_visited.popleft()
        
        for i in range(n+1):
            if not visited[i] and abs(graph[i][0] - node[0]) + abs(graph[i][1] - node[1]) <= 1000: 
                need_visited.append(graph[i])
                visited[i] = True
                
    if visited[-1]:
        return "happy"
    else:
        return "sad"


t = int(input())
result = []

for _ in range(t):
    n = int(input())
    
    start = list(map(int, input().split()))
    graph = []
    for _ in range(n+1):
        graph.append(list(map(int, input().split())))
    
    visited = [False] * (n + 1)

    result.append(bfs(start))
    
for i in result:
    print(i)