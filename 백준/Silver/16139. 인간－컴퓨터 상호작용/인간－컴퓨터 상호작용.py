import sys

s = sys.stdin.readline()
q = int(sys.stdin.readline())

for i in range(q):
    a, l, r = map(str, sys.stdin.readline().split())
    l, r = int(l), int(r)
    count = 0
    for j in range(l,r+1):
        if s[j] == a:
            count += 1
    print(count)