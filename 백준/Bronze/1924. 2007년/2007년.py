m, d = map(int, input().split())
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
print(week[(sum(day[:m - 1]) + d) % 7])