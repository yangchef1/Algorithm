import heapq, sys

n = int(input())
course = []

for _ in range(n):
    course.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
course.sort()
room = [course[0][1]]

for i in range(1, n):
    if room[0] > course[i][0]:
        heapq.heappush(room, course[i][1])
    else:
        heapq.heappushpop(room, course[i][1])

print(len(room))