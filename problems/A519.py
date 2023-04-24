d = {"q": 9, "r": 5, "b": 3, "n": 3, "p": 1}

b = 0
c = 0
for _ in range(8):
    a = input()
    for p in a:
        if p == '.':
            continue
        if p.lower() == "k":
            continue
        if p.upper() == p:
            c += d[p.lower()]
            continue
        b += d[p]
print("Draw" if b == c else "White" if c > b else "Black")