N, M = map(int, input().split())
if N:
    books = list(map(int, input().split()))
    i = 0
    cnt = 1
    box_space = M
    while i < len(books):
        if books[i] <= box_space:
            box_space -= books[i]
        else:
            cnt += 1
            box_space = M - books[i]
        i += 1

    print(cnt)
else:
    print(0)