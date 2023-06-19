s = input()
an = 1

for i in range(len(s)//2 + 1):
    if s[i] == s[len(s)-i-1]:
        pass
    else:
        an = 0
        break
    
print(an)