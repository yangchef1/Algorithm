n = int(input())
li = list(map(int, input().split()))
s = set(li)
k = int(input())
cnt = 0

for i in li:
    if k - i in s:
        cnt += 1

print(cnt // 2)