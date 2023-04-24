n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

while (sum(a) / len(a)) * 2 < (k * 2) - 1:
    a.append(k)
    
print(len(a) - n)