T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if (x2-x1)**2 + (y2-y1)**2 > (r1 + r2)**2:
        print(0)
    elif (x2-x1)**2 + (y2-y1)**2 == (r1 + r2)**2:
        print(1)
    else:
        if x1 == x2 and y1 == y2:
            if r1 == r2:
                print(-1)
            else:
                print(0)
        else:
            
            if (min(r1, r2) + round(((x2-x1)**2 + (y2-y1)**2)**0.5))**2 > max(r1, r2)**2:
                print(2)
            elif (min(r1, r2) + round(((x2-x1)**2 + (y2-y1)**2)**0.5))**2 == max(r1, r2)**2:
                print(1)
            else:
                print(0)
