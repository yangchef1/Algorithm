n = input()
s = [0] * 10

for i in n:
    s[int(i)] += 1

temp = ((s[6] + s[9]) // 2) + ((s[6] + s[9]) % 2)
s[6], s[9] = temp, temp

print(max(s))