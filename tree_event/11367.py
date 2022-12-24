for _ in range(int(input())):
    s, n = input().split()
    n = int(n)
    if n >= 97: result = "A+"
    elif n >= 90: result = "A"
    elif n >= 87: result = "B+"
    elif n >= 80: result = "B"
    elif n >= 77: result = "C+"
    elif n >= 70: result = "C"
    elif n >= 67: result = "D+"
    elif n >= 60: result = "D"
    else: result = "F"
    print(s, result)