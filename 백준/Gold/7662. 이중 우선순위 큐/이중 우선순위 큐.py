import sys
import heapq

t = int(sys.stdin.readline())

for _ in range(t):
    count = [0]*1000000
    heap_min = []
    heap_max = []
    n = int(sys.stdin.readline())
    for i in range(n):
        a, b = list(map(str,sys.stdin.readline().split()))
        b = int(b)
        if a == 'I':
            heapq.heappush(heap_min, (b,i))
            heapq.heappush(heap_max, (-b,i))
            count[i] = 1
        else:
            if b == -1:
                while heap_min and count[heap_min[0][1]] == 0:
                    heapq.heappop(heap_min)
                if heap_min:
                    k, p = heapq.heappop(heap_min)
                    count[p] = 0
            else:
                while heap_max and count[heap_max[0][1]] == 0:
                    heapq.heappop(heap_max)
                if heap_max:
                    k, p = heapq.heappop(heap_max)
                    count[p] = 0

    while heap_min and count[heap_min[0][1]] == 0: heapq.heappop(heap_min)
    while heap_max and count[heap_max[0][1]] == 0: heapq.heappop(heap_max)

    if not heap_min:
        print("EMPTY")
    else:
        print(-heap_max[0][0], heap_min[0][0])