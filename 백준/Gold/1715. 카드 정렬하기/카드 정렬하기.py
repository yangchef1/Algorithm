import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)

cum = 0
for _ in range(n - 1):
  f = heapq.heappop(cards)
  s = heapq.heappop(cards)
  cum += (f + s)
  heapq.heappush(cards, f + s)
  
print(cum)