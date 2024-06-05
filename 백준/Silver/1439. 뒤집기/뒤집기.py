s = input()
cnt = 1

for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        cnt += 1
        
print(cnt // 2)