for i in range(int(input())):
    a = input()
    b = False
    d = 0

    if a == "^":
        print("1")
        continue

    for c in a:
        if c == '^':
            b = True
            continue

        if b:
            b = False
            continue

        d += 1    
    d += 1 if a[-1] == "_" else 0

    print(d)