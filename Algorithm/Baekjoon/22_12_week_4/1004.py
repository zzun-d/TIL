T = int(input())
for _ in range(T):
    planet = {}
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for i in range(n):
        planet[i] = list(map(int, input().split()))
    S = set()
    E = set()
    for k, v in planet.items():
        cx, cy, r = v
        if (cx - x1)**2 + (cy - y1)**2 < r**2:
            S.add(k)
        if (cx - x2)**2 + (cy - y2)**2 < r**2:
            E.add(k)
    print(len(S-E) + len(E-S))
    