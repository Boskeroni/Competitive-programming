for _ in range(int(input())):
    n = int(input())
    # [0, 3, 4, 4, 3]
    a = list(map(int, input().split()))

    if n < 3:
        for _ in range(n):
            print(a[0], end=" ")
        continue

    b = [a[0]]

    for i in range(n-2):
        if a[i] <= a[i+1]:
            b.append(a[i])
            continue

        b.append(a[i+1])
    b.append(a[-1])
    for i in b:
        print(i, end=" ")
