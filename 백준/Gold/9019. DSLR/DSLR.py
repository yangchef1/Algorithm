import sys
from collections import deque

t = int(sys.stdin.readline())


def Left(n):
    return (n*10 + n//1000)%10000


def Right(n):
    return (n%10)*1000+n//10


def bfs(a, b):
    need_visited = deque()
    need_visited.append((a,''))
    visited = [0] * 10000

    while need_visited:
        node, s = need_visited.popleft()
        if node == b:
            return s

        if node*2 <= 9999:
            if visited[node*2] == 0 or visited[node*2] > visited[node] + 1:
                need_visited.append((node*2,s+'D'))
                visited[node*2] = visited[node] + 1
        else:
            if visited[(node*2)%10000] == 0 or visited[(node*2)%10000] > visited[node] + 1:
                need_visited.append(((node*2)%10000,s+'D'))
                visited[(node*2)%10000] = visited[node] + 1

        if node == 0:
            if visited[9999] == 0 or visited[9999] > visited[node] + 1:
                need_visited.append((9999,s+'S'))
                visited[9999] = visited[node] + 1
        else:
            if visited[node - 1] == 0 or visited[node - 1] > visited[node] + 1:
                need_visited.append((node - 1,s+'S'))
                visited[node - 1] = visited[node] + 1

        if visited[Left(node)] == 0 or visited[Left(node)] > visited[node] + 1:
            need_visited.append((Left(node),s+'L'))
            visited[Left(node)] = visited[node] + 1

        if visited[Right(node)] == 0 or visited[Right(node)] > visited[node] + 1:
            need_visited.append((Right(node),s+'R'))
            visited[Right(node)] = visited[node] + 1


for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a,b))