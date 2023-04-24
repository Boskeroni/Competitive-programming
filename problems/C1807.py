for _ in range(int(input())):
    _ = input()
    s = input()
    d = {s[0]: "1"}
    b = True

    for i, c in enumerate(s[1::]):
        if c in d:
            w = d[c]
            if d[s[i]] == w:
                b = False
                print("No")
                break
            continue
        d[c] = "1" if d[s[i]] == "0" else "0"
    if b:
        print("YES")
    