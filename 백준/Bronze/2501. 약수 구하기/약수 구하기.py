n, k = map(int, input().split())
cnt = 1

for i in range(1, n+1):
    if n % i == 0:
        if cnt == k:
            print(i)
            exit(0)
        cnt += 1 
print(0)