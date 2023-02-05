import sys
from collections import deque

n, m, r = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited1 = [False]*(n+1)
visited2 = [False]*(n+1)
result1 = []
result2 = []

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs (graph,i):
    need_visited = deque()
    need_visited.append(i)
    while need_visited:
        node = need_visited.pop()
        if not visited1[node]:
            result1.append(node)
            visited1[node] = True
            need_visited.extend(graph[node])


def bfs (graph,i):
    need_visited = deque()
    need_visited.append(i)
    while need_visited:
        node = need_visited[0]
        del(need_visited[0])
        if not visited2[node]:
            result2.append(node)
            visited2[node] = True
            need_visited.extend(graph[node])



for i in graph:
    i.sort()
bfs(graph,r)
for i in graph:
    i.reverse()
dfs(graph,r)

for i in result1:
    print(i, end = ' ')
print()
for i in result2:
    print(i, end = ' ')