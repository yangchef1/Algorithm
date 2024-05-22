t = int(input())
button = [300, 60, 10]

if t % 10 != 0:
    print(-1)
    exit(0)

for i in button:
    print(t // i, end = " ")
    t %= i