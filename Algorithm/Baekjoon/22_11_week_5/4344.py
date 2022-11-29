T = int(input())
for _ in range(T):
    lst = list(map(int, input().split()))
    aver = sum(lst[1:])/lst[0]
    cnt = 0
    for score in lst[1:]:
        if score > aver:
            cnt += 1
    print(f'{cnt/lst[0]*100:0.3f}%')