arr = [list(input()) for _ in range(8)]
queue = [(7, 0)]
tmp = False
while queue:
    nxt = set()
    for _ in range(len(queue)):
        i, j = queue.pop()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < 8 and 0 <= nj < 8 and arr[ni][nj] == '.':
                if ni > 0 and arr[ni-1][nj] == '#':
                    continue
                elif ni == 0 and nj == 7:
                    tmp = True
                    break
                nxt.add((ni, nj))
    arr.pop()
    arr = [['.']*8] + arr
    queue = list(nxt)
    if tmp:
        break
if tmp:
    print(1)
else:
    print(0)