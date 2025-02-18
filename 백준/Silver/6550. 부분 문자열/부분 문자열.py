while True:
    try:
        s, t = input().split()
        idx = 0
        for i in t:            
          if i == s[idx]:
            idx += 1
            
          if idx == len(s):
            print("Yes")
            break
            
        if idx < len(s):
          print("No")
    except EOFError:
        break