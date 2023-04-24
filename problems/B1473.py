from math import lcm

for _ in range(int(input())):
    a = input()
    b = input()
    l = lcm(len(a), len(b))
    a = a * (l // len(a))
    b = b * (l // len(b))
    if a == b:
        print(a)
    else:
        print(-1)