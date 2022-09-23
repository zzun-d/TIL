def solution(n, info):
    def f(i, cnt, ry, ap):
        if cnt > n:
            return

        elif cnt == n or i > 10:
            if ry > ap:

                if result.get(ry-ap):
                    if n-cnt:
                        result[ry-ap].append([n-cnt]+board[::-1][1:])
                    else:
                        result[ry-ap].append([0]*(11-len(board)) + board[::-1])
                else:
                    if n-cnt:
                        result[ry-ap] = [[n-cnt] + board[::-1][1:]]
                    else:
                        result[ry-ap] = [[0]*(11-len(board))+ board[::-1]]
        else:
            board.append(info[i] + 1)
            if info[i]:
                f(i + 1, cnt + info[i] + 1, ry + (10 - i), ap - (10 - i))
            else:
                f(i + 1, cnt + info[i] + 1, ry + (10 - i), ap)
            board.pop()
            board.append(0)
            f(i + 1, cnt, ry, ap)
            board.pop()

    result = {}
    apeach = 0
    board = []
    for i in range(10):
        apeach += (10 - i) if info[i] else 0

    f(0, 0, 0, apeach)

    if result:
        posList = result[max(list(result.keys()))]
        posList.sort(reverse=True)
        answer = posList[0][::-1]
    else:
        answer = [-1]

    return answer

print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
