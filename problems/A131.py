a = input()
if a.upper() == a:
    print(a.lower())
elif a[0] == a[0].lower() and a[1::].upper() == a[1::]:
    print(a.title())
else:
    print(a)
