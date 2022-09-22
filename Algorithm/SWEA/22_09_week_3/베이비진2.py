def baby(lst):
    if lst.count(3):
        return True

    for j in range(8):
        if lst[j] and lst[j+1] and lst[j+2]:
            return True
    return False

T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    A = [0]*10
    B = [0]*10
    ans = 0
    for i in range(0, 12, 2):
        A[cards[i]] += 1
        if baby(A):
            ans = 1
            break
        B[cards[i+1]] += 1
        if baby(B):
            ans = 2
            break
    print(f'#{tc} {ans}')