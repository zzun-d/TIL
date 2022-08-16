N = int(input())
lst = [i for i in range(1, N+1)]
while True:
    if len(lst) == 1:
        break
    elif len(lst)%2:
        lst = [0] + [lst[i] for i in range(1, len(lst), 2)]
    else:
        lst = [lst[i] for i in range(1, len(lst), 2)]
    
print(*lst)