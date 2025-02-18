encrypt = input()
n = int(input())
words = [input() for _ in range(n)]

for w in words:
  for i in range(26):
    decrypt = "".join(chr(ord(c) + i if ord(c) + i <= ord("z") else ord(c) + i - 26) for c in w)
    if decrypt in encrypt:
      print("".join(chr(ord(c) - i if ord(c) - i >= ord("a") else ord(c) - i + 26) for c in encrypt))
      exit(0)