import itertools

T = int(input())

for _ in range(T):
    N = int(input())
    x_total = 0
    y_total = 0
    coordi = []
    mn = 10**6
    for _ in range(N):
        x, y = map(int, input().split())
        x_total += x
        y_total += y
        coordi.append((x, y))
    for combi in itertools.combinations(coordi, N//2):
        x_add_sm = 0
        y_add_sm = 0
        for c in combi:
            x_add_sm += c[0]
            y_add_sm += c[1]
        x_sub_sm = x_total - x_add_sm
        y_sub_sm = y_total - y_add_sm
        l = ((x_add_sm - x_sub_sm)**2 + (y_add_sm - y_sub_sm)**2)**0.5
        if mn > l:
            mn = l
    
    print(mn)
