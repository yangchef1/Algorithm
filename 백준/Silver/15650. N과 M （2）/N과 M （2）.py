import sys


def backtracking(n,m,start):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    for i in range(start, n+1):
        if i not in ans:
            ans.append(i)
            backtracking(n,m,i+1)
            ans.pop()


n, m = map(int, sys.stdin.readline().split())
ans = []
backtracking(n,m,1)