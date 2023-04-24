for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    
    i = 1
    while True:
        if i not in y:
            x -= 1
            if x == -1:
                break            
        i += 1
    print(i - 1)