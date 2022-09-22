T = int(input())

for tc in range(1, T+1):
    two = list(map(int, list(input())))
    three = list(map(int, list(input())))

    two_lst = []
    for i in range(len(two)):
        if two[i]:
            two[i] = 0
        else:
            two[i] = 1
        v = 0
        for j in range(len(two)):
            v += (2**(len(two)-j-1))*two[j]
        two_lst.append(v)

        if two[i]:
            two[i] = 0
        else:
            two[i] = 1

    tmp = False
    for i in range(len(three)):
        if three[i] == 2:
            for k in [0, 1]:
                three[i] = k
                v = 0
                for j in range(len(three)):
                    v += (3**(len(three)-j-1))*three[j]
                if v in two_lst:
                    tmp = True
                    break
            three[i] = 2

        elif three[i] == 1:
            for k in [0, 2]:
                three[i] = k
                v = 0
                for j in range(len(three)):
                    v += (3**(len(three)-j-1))*three[j]
                if v in two_lst:
                    tmp = True
                    break
            three[i] = 1

        else:
            for k in [1, 2]:
                three[i] = k
                v = 0
                for j in range(len(three)):
                    v += (3**(len(three)-j-1))*three[j]
                if v in two_lst:
                    tmp = True
                    break
            three[i] = 0

        if tmp:
            break
    print(f'#{tc} {v}')

