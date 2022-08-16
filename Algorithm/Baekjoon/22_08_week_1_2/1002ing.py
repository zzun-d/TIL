t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    c_d = int(round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 1))
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        if c_d > r1 + r2:
            print(0)
        elif c_d == r1 + r2:
            print(1)
        else:
            if abs(r1 - r2) > c_d:
                print(0)
            elif abs(r1 - r2) == c_d:
                print(1)
            else:
                print(2)