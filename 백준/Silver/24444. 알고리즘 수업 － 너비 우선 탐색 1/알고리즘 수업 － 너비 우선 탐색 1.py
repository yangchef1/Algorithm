import sys
from collections import deque

n, m, r = map(int,sys.stdin.readline().split())
result = [0]*(n+1)
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs (graph, i):
    global count
    need_visited = deque()
    need_visited.append(i)
    while need_visited:
        node = need_visited.popleft()
        if not visited[node]:
            visited[node] = True
            count += 1
            result[node] = count
            need_visited.extend(graph[node])


for i in graph:
    i.sort()


count = 0

bfs(graph,r)

for i in range(1,n+1):
    print(result[i])