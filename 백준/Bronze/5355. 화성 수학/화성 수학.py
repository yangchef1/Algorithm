t = int(input())

for _ in range(t):
    cal = list(input().split())
    ans = float(cal[0])
    
    for i in range(1, len(cal)):
        if cal[i] == '@':
            ans *= 3
        elif cal[i] == '%':
            ans += 5
        elif cal[i] == '#':
            ans -= 7
    
    print('{:.2f}'.format(ans))