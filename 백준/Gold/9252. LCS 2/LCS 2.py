a = list(input())
b = list(input())

DP = [[0]*(len(b) + 1) for _ in range(len(a) + 1)]
arr = [['']*(len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i - 1] == b[j - 1]:
            DP[i][j] = DP[i-1][j-1] + 1
            arr[i][j] = arr[i-1][j-1] + a[i-1]
        elif len(arr[i-1][j]) >= len(arr[i][j-1]):
            DP[i][j] = DP[i-1][j]
            arr[i][j] = arr[i-1][j]
        else:
            DP[i][j] = DP[i][j-1]
            arr[i][j] = arr[i][j-1]

if DP[len(a)][len(b)] == 0:
    print(0)
else:
    print(DP[len(a)][len(b)])         
    print(arr[len(a)][len(b)])