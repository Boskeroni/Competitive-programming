for _ in range(int(input())):
    _ = input()
    a = list(map(int, input().split()))
    _ = input()
    b = list(map(int, input().split()))
    
    c = 0
    cb = 0
    d = 0
    db = 0
    for i in a:
        c += i
        if c > cb:
            cb = c
    for i in b:
        d += i
        if d > db:
            db = d
    print(db + cb)