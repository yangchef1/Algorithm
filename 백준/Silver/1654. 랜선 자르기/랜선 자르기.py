import sys

k, n = map(int, sys.stdin.readline().split())
a = []
for i in range(k):
    a.append(int(sys.stdin.readline()))

start = 1
end = max(a)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in a:
        sum += i // mid
    if sum < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)