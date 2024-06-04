e, s, m = map(int, input().split())
year = s

while True:
    if (year - e) % 15 == 0 and (year - m) % 19 == 0:
        print(year)
        break
    year += 28