c = []
d = ""
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if a != b:
        d = "rated"
        continue
    if d != "":
        continue
    if len(c) == 0:
        c.append(a)
        continue
    if c[-1] < a:
        d = "unrated"
    c.append(a)
if d == "": d = "maybe"
print(d)