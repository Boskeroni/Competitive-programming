for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    a = input()
    used = False

    for c in a:
        if used or int(c) >= d:
            print(c, end="")
            continue
        used = True
        print(f"{d}{c}", end="")
    if not used:
        print(d, end="")
    print()