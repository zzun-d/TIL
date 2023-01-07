N = int(input())
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
n = '11'

while True:
    if len(lst) >= N:
        print(lst[N-1])
        break
    elif len(n) > 6:
        print(-1)
        break

    for i in range(len(n)-1):
        if n[i] <= n[i+1]:
            if n[i] == '9' and i:
                [i-1]


            n = n[:i] + str(int(n[i])+1)
            for j in range(len(len(n[i+1:])), 0, -1):
                n += int(n[i])+1
            break
    else:
        lst.append(n)
        n = str(int(n)+1)