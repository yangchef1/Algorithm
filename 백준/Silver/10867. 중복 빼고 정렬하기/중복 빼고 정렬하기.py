n = int(input())
print(" ".join(map(str, sorted(list(set(map(int, input().split())))))))