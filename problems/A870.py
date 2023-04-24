_ = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = float('inf')
for c in a:
    if c in b:
        l = l if c > l else c
if l == float('inf'):
    a = min(a)
    b = min(b)
    
    l = int(f"{a}{b}" if a < b else f"{b}{a}")
print(l)