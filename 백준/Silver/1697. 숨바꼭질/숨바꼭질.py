from collections import deque

def bfs(visited, dis, start, dest):
    need_visited = deque([start])
    visited[start] = True
    
    while need_visited:
        node = need_visited.popleft()
        
        if node == dest:
            return
        
        temp = [node * 2, node - 1, node + 1] 
        
        for i in temp:
            if i <= 100000 and i >= 0 and not visited[i]:
                visited[i] = True
                need_visited.append(i)
                dis[i] = dis[node] + 1                    

s, d = map(int, input().split())
visited = [False] * 100001
dis = [0] * 100001

bfs(visited, dis, s, d)

print(dis[d])