a, b, c, d, e, f = map(int, input().split())

print((c*e - b*f) // (a*e - b*d), (c*d - f*a) // (b*d - a*e))
