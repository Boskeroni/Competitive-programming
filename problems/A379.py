a, b = list(map(int, input().split()))
s = 0
r = 0
while a != 0:
    s += a
    r += a 
    a = r // b
    r = r % b
print(s)