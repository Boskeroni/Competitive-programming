a = int(input())
b = list(map(int, input().split()))

d = abs(b[0] - b[a-1])
e = [1, a]
for i, c in enumerate(b[1::]):
    f = abs(c - b[i])
    if f < d:
        d = f
        e = [i+1, i+2]
print(e[0], e[1])