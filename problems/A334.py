a = int(input())
b = a ** 2

for i in range(1, b//2+1):
    print(i, (b-i)+1, "", end="")
    if i % (a // 2) == 0:
        print()