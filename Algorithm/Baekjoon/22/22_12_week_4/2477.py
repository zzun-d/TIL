K = int(input())
rand = {}
for i in range(6):
    d, l = map(int, input().split())
    if rand.get(d):
        rand[d].append((i, l))
    else:
        rand[d] = [(i, l)]

WH = []
check = []
for i in range(1, 5):
    if len(rand[i]) == 1:
        WH.append(rand[i][0][1])
    else:
        check += rand[i]
check.sort()
if check[1][0] + 1 == check[2][0]:
    if check[0][0] + 3 == check[3][0]:
        wh = [check[1][1], check[2][1]]
    else:
        if check[0][0] + 1 == check[1][0]:
            wh = [check[0][1], check[1][1]]
        else:
            wh = [check[2][1], check[3][1]]
else:
    wh = [check[0][1], check[3][1]]

print(K*(WH[0]*WH[1] - wh[0]*wh[1]))