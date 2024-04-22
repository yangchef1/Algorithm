from collections import deque

def bfs(start, visited):
    need_visited = deque([(start, 0)])
    
    while need_visited:
        node, d = need_visited.popleft()
      
        if node == 1:
            return d
        
        next_nodes = [node - 1]
        
        if node % 2 == 0:
            next_nodes.append(node // 2)
        if node % 3 == 0:
            next_nodes.append(node // 3)
            
        for next_node in next_nodes:
            if visited[next_node] == 0:
                visited[next_node] = node   
                need_visited.append((next_node, d + 1))

n = int(input())
visited = [0] * (n + 1)
path = [1]
ans = bfs(n, visited)

print(ans)

for i in range(ans):
    path.append(visited[path[-1]])

print(" ".join(map(str, path[::-1])))