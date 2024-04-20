from collections import deque

def bfs(dis, visited, start, dest):
    need_visited = deque([start])
    
    while need_visited:
        node = need_visited.popleft()
       
        if node == dest:
            return
        
        next_nodes = [node * 2, node - 1, node + 1]
        
        for next_node in next_nodes:
            if next_node >= 0 and next_node <= 100000 and visited[next_node] < 0:
                dis[next_node] = min(dis[next_node], dis[node] + 1)
                visited[next_node] = node
                need_visited.append(next_node)
                
n, k = map(int, input().split())
dis = [float('inf')] * 100001
visited = [-1] * 100001
dis[n] = 0

bfs(dis, visited, n, k)
shortest = dis[k]

result = [k]

print(shortest)

for i in range(shortest):
    result.append(visited[result[-1]])
    
for i in range(shortest + 1):    
    print(result.pop(), end = " ")