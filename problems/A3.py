m = "abcdefgh"

a = input()
b = input()

y_d = int(a[1]) - int(b[1])
x_d = m.index(a[0]) - m.index(b[0])

maxi = abs(y_d) if abs(y_d) > abs(x_d) else abs(x_d)
print(maxi)

while maxi != 0:
    d = ""
    d += "R" if x_d < 0 else "L" if x_d > 0 else ""
    if x_d > 0: x_d -= 1
    if x_d < 0: x_d += 1
    d += "U" if y_d < 0 else "D" if y_d > 0 else ""
    if y_d > 0: y_d -= 1
    if y_d < 0: y_d += 1
    maxi -= 1
    print(d)
    