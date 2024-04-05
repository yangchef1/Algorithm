n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())))
sum = 0
for i, j in zip(A, B):
    sum += i * j
print(sum)