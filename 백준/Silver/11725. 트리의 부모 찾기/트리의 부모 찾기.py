import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

need_visited = deque()
answer = [0] * (n+1)


need_visited.append(1)
visited[1] = True

while need_visited:
    node = need_visited.popleft()
    for i in graph[node]:
        if not visited[i]:
            answer[i] = node
            need_visited.append(i)
            visited[i] = True

for i in range(2,n+1):
    print(answer[i])