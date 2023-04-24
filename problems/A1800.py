b = "meow"
for _ in range(int(input())):
    _ = input()
    a = input().lower()
    c = 0
    if a[0] != "m" or a[-1] != "w":
        print("NO")
        continue
    
    for i in a:
        if i == b[c]:
            continue
        if c == 3:
            print("NO")
            break
        if i == b[c+1]:
            c += 1
            continue
        print("NO")
        break
    else:
        print("YES")