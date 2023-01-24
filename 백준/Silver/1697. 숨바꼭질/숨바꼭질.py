import sys
from collections import deque

x, y = map(int,sys.stdin.readline().split())

if x == y:
    print(0)
    exit(0)

graph = [0]*400001

need_visited = deque()
need_visited.append(x)

while need_visited:
    if graph[y] != 0:
        break
    k = need_visited.popleft()
    if k+1 <= 400000:
        if graph[k+1] == 0:
            graph[k + 1] = graph[k] + 1
            need_visited.append(k + 1)
    if k <= 400000:
        if graph[k-1] == 0:
            graph[k - 1] = graph[k] + 1
            need_visited.append(k - 1)
    if k <= 200000 and k > 0:
        if graph[k*2] == 0:
            graph[k * 2] = graph[k] + 1
            need_visited.append(k * 2)

print(graph[y])