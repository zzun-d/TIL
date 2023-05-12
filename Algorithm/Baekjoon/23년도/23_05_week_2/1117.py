W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

w = W - f

h = H // (c+1)

l_color = c+1

ans = (x2 - x1) * (y2 - y1) * l_color

if f < w:

    if x1 <= f:
        ans += (min(f, x2) - x1) * (y2-y1) * l_color


elif f == w:
    ans *= 2

else:
    if x1 <= w:
        ans += (min(w, x2) - x1) * (y2-y1) * l_color

print(W*H - ans)
