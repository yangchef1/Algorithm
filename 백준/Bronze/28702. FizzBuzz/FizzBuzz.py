s = [input() for _ in range(3)]
result = 0

for i in range(3):
  if 'z' not in s[i]:
    result = int(s[i]) + (3 - i)
    
if result % 3 == 0:
  print('Fizz', end="")

if result % 5 == 0:
  print('Buzz', end="")
  
if result % 3 != 0 and result % 5 != 0:
  print(result)