import sys
d = [0] * 41
count_z = [0]*41
count_o = [0]*41
count_z[0] = count_o[1] = 1


def fib(n):
    if d[n] != 0:
        return d[n]
    else:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            d[n] = fib(n-1) + fib(n-2)
            count_z[n] = count_z[n-1] + count_z[n-2]
            count_o[n] = count_o[n - 1] + count_o[n - 2]
            return fib(n-1) + fib(n-2)


n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    k = fib(a)
    print(count_z[a],count_o[a])