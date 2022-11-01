def divide(arr):
    l = len(arr)
    if l == 1:
        return arr[0][0]
    lst = []
    for si, sj in [(0, 0), (0, l//2), (l//2, 0), (l//2, l//2)]:
        tmp = False
        k = arr[si][sj]
        for i in range(si, si+l//2):
            for j in range(sj, sj+l//2):
                if k != arr[i][j]:
                    tmp = True
                    narr = [arr[ni][sj:sj+l//2] for ni in range(si, si+l//2)]
                    lst.append(divide(narr))
                if tmp:
                    break
            if tmp:
                break
        if not tmp:
            lst.append(k)
    l_set = set(lst)
    if len(l_set) == 1 and len(lst[0]) == 1:
        return lst[0]
    return '(' + ''.join(lst) + ')'
N = int(input())
ARR = [input() for _ in range(N)]
print(divide(ARR))