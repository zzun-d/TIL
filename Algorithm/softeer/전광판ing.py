swich_dict = {
    0 : [0, 4, 3, 3, 4, 3, 2, 2, 1, 2, 6],
    1 : [4, 0, 5, 3, 2, 5, 6, 2, 5, 4, 2],
    2 : [3, 5, 0, 2, 5, 4, 3, 5, 2, 3, 5],
    3 : [3, 3, 2, 0, 3, 2, 3, 3, 2, 1, 5],
    4 : [4, 2, 5, 3, 0, 3, 4, 2, 3, 2, 4],
    5 : [3, 4, 4, 2, 3, 0, 1, 3, 2, 1, 5],
    6 : [2, 6, 3, 3, 4, 1, 0, 4, 1, 2, 6],
    7 : [2, 2, 5, 3, 2, 3, 4, 0, 3, 2, 4],
    8 : [1, 5, 2, 2, 3, 2, 1, 3, 0, 1, 7],
    9 : [2, 4, 3, 1, 2, 1, 2, 2, 1, 0, 6],
}

t = int(input())
for _ in range(t):
    cnt = 0
    num_1, num_2 = input().split()
    if len(num_1) > len(num_2):
        num_2 = '.' * (len(num_1) - len(num_2)) + num_2
    elif len(num_2) > len(num_1):
        num_1 = '.' * (len(num_2) - len(num_1)) + num_1
    
    
    for n_1, n_2 in zip(num_1, num_2):
        if n_1 == '.':
            cnt += swich_dict[int(n_2)][-1]
        elif n_2 == '.':
            cnt += swich_dict[int(n_1)][-1]
        else:
            n_1 = int(n_1)
            n_2 = int(n_2)
            cnt += swich_dict[n_1][n_2]
    print(cnt)


    