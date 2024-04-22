n, k = map(int, input().split())
stud = list(map(int, input().split()))
diff = []

for i in range(1, n):
    diff.append(stud[i] - stud[i - 1])

diff.sort(reverse=True)

ans = stud[-1] - stud[0]

for i in range(k - 1):
    ans -= diff[i]

print(ans)