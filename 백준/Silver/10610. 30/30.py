n = int("".join(sorted(input(), key=int, reverse=True)))
print(n if n % 30 == 0 else -1)