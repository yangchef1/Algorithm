n = int(input())
s = map(int, input().split())
c_s = 0
m_s = 0

for i in s:
    if i == 0:
        m_s = max(m_s, c_s)
        c_s = 0
    else:
        c_s += 1

print(max(m_s, c_s))