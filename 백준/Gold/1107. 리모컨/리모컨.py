import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
button = [0,1,2,3,4,5,6,7,8,9]

if m != 0:
    broken = list(map(int, sys.stdin.readline().split()))
    for i in broken:
        button.remove(i)

if n - 100 < 0:
    w = 100 - n
else:
    w = n - 100

if m == 10:
    print(w)
    exit(0)

result= 0
k, p = n, n

for i in range(1000000):
    cnt1 = 0
    cnt2 = 0
    ns1 = str(k)
    ns2 = str(p)

    for j in ns2:
        if int(j) not in button:
            cnt2 += 1
            break
    if cnt2 == 0:
        result = p
        break
    elif n - i >= 0:
        p = n - i

    for j in ns1:
        if int(j) not in button:
            cnt1 += 1
            break
    if cnt1 == 0:
        result = k
        break
    else:
        k = n + i

if n - result < 0:
    s = result - n
else:
    s = n - result

print(min([w,s+len(str(result))]))