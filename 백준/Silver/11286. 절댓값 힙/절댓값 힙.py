import sys
import heapq

heap = []
n = int(sys.stdin.readline())

for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(a),a))