s = input()
ans = 0

for i in range(len(s)):
    if ord(s[i]) < 65:
        ans += (int(s[i]) * (16 ** (len(s) - (i + 1))))
    else:
        ans += ((ord(s[i]) - 55) * (16 ** (len(s) - (i + 1))))
        
print(ans)        