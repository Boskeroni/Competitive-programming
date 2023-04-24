for _ in range(int(input())):
    _ = input()
    a = list(map(int, input().split()))
    
    for i, c in enumerate(a):
        if c > i + 1:
            continue
        print("YES")
        break
    else:
        print("NO")