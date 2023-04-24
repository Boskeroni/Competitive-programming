a = input()
b = input()

l = len(b) if len(a) > len(b) else len(a)
i = 1
if l == 0:
    print(len(a) if len(a) > len(b) else len(b))
else:
    while a[-i] == b[-i]:
        i += 1
        if i > l:
            break
    i -= 1

    c = (len(a) - i) + (len(b) - i)
    print(c)