for _ in range(int(input())):
    n, k = map(int, input().split())

    if n % 2 == 0:
        print("Yes")
        continue

    if k % 2 == 0:
        print("No")
        continue

    if n - k >= 0:
        print("Yes")
        continue

    print("No")