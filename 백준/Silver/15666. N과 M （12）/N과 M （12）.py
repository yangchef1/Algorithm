import sys


def back():
    rem = 0

    if len(ans) == m:
        print(' '.join(map(str,ans)))
        return

    for i in range(n):
        if rem != arr[i]:
            if ans:
                if ans[-1] <= arr[i]:
                    ans.append(arr[i])
                    rem = arr[i]
                    back()
                    ans.pop()
                else:
                    pass
            else:
                ans.append(arr[i])
                rem = arr[i]
                back()
                ans.pop()


n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = []

back()