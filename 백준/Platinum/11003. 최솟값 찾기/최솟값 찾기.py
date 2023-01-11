import sys
from collections import deque

n, l = map(int, sys.stdin.readline().split())

d_li = [0] * n

a_li = list(map(int, sys.stdin.readline().split()))

li = deque()

for i in range(n):
    while li and li[-1][1] > a_li[i]:
        li.pop()

    while li and i - li[0][0] >= l:
        li.popleft()

    li.append([i,a_li[i]])
    d_li[i] = li[0][1]


print(*d_li)