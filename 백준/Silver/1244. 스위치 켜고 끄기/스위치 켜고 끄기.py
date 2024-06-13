n = int(input())
switch = [0] + list(map(int, input().split()))

m = int(input())
for _ in range(m):
    s, num = map(int, input().split())
    
    if s == 1:
        for i in range(num, n + 1, num):
            if switch[i] == 0:
                switch[i] = 1
            else: 
                switch[i] = 0
    else:
        for i in range(1, n):
            if num <= i or i > n - num or switch[num - i] != switch[num + i]:
                for j in range(num - (i - 1), num + i):
                    if switch[j] == 0:
                        switch[j] = 1
                    else: 
                        switch[j] = 0
                break

for i in range(1, n + 1):
    print(switch[i], end = " ")
    if i % 20 == 0:
        print()   