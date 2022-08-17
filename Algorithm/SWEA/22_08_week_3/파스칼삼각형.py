T = int(input())
for t in range(1, T+1):
    n = int(input())
    lst = [1]
    print(f'#{t}')
    print(*lst)
    for _ in range(n-1):
        n_lst = []              # 다음 리스트 초기화
        n_lst.append(lst[0])    # 다음 리스트의 처음 값은 전 리스트의 처음 값
        for i in range(len(lst)-1):     # 다음 리스트의 2번째 요소부터 전 리스트 값 더해서 넣어줌
            num = lst[i] + lst[i+1]
            n_lst.append(num)
        n_lst.append(lst[-1])   # 다음 리스트의 마지막 값은 전 리스트의 마지막 값
        print(*n_lst)
        lst = n_lst
