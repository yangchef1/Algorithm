import sys
from collections import deque

l, s = map(int,sys.stdin.readline().split())

dis = [0]*101
ladder = []
snake = []

for i in range(l):
    ladder.append(list(map(int, sys.stdin.readline().split())))

for i in range(s):
    snake.append(list(map(int, sys.stdin.readline().split())))

need_visited = deque()
need_visited.append(1)

while need_visited:
    k = need_visited.popleft()
    li = []
    for i in range(1,7):
        cnt = 0
        nk = k + i
        if nk <= 100:
            if dis[nk] == 0 or dis[nk] > dis[k] + 1:
                dis[nk] = dis[k] + 1
            for j in range(l):
                if ladder[j][0] == nk:
                    cnt += 1
                    if dis[ladder[j][1]] > dis[nk] or dis[ladder[j][1]] == 0:
                        dis[ladder[j][1]] = dis[nk]
                        need_visited.append(ladder[j][1])
            if cnt == 0:
                for j in range(s):
                    if snake[j][0] == nk:
                        cnt += 1
                        if dis[snake[j][1]] > dis[nk] or dis[snake[j][1]] == 0:
                            dis[snake[j][1]] = dis[nk]
                            need_visited.append(snake[j][1])
            if cnt == 0:
                li.append(nk)
    need_visited.append(max(li))
    if dis[100] != 0:
        break

print(dis[100])