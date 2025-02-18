key = input()
encrypt = input()

sorted_key = sorted(key)
board = [[k] for k in key]
length = len(encrypt) // len(key)

for sk, idx in zip(sorted_key, range(len(key))):
  for line in board:
    if line[0] == sk and len(line) == 1:
      line.extend(encrypt[idx*length:(idx + 1)*length])
      break

for i in range(1, length + 1):
  for line in board:
    print(line[i], end="")