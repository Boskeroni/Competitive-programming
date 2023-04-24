for _ in range(int(input())):
    a = input()
    b = list(map(int, input().split()))

    mi = sum([i for i in b if i % 2 == 0])
    bi = sum([i for i in b if i % 2 == 1])

    if mi > bi:
        print("YES")
        continue
    print("NO")