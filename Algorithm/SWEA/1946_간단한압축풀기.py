T = int(input())

for i in range(T):
    C = int(input())
    print(f'#{i+1}')
    answer = ''
    for j in range(C):
        a, n = input().split()
        n = int(n)
        answer += a*n
    L = len(answer)
    for j in range(L//10 + 1):
        if j + 1 <= L//10:
            print(answer[j*10:j*10+10])
        else:
            print(answer[j*10:])
        
            
